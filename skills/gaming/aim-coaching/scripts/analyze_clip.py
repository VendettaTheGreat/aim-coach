#!/usr/bin/env python3
"""Analyze crosshair-to-target offset in a KovaaK's gameplay clip.

Usage: python analyze_clip.py <video_path> [--fps 5] [--threshold 40]

Outputs:
  - Per-frame offset (dx, dy, distance) from screen center to target
  - On-target rate (% frames <15px offset)
  - Speed-change events (dx sign reversals with magnitude >20px)
  - Vertical bias (mean dy)
  - Classification breakdown (on-target / horizontal lag / horizontal lead / vertical drift)

Methodology:
  1. Convert HEVC to H264 if needed (ffmpeg -c:v libx264 -preset fast -crf 18 -an)
  2. Extract frames at 5fps (ffmpeg -vf fps=5)
  3. Detect target bot as dark pixels (grayscale < threshold) in Y range 200-600
  4. Use median (not mean) for target position -- robust to outliers from shadows/UI
  5. Measure offset from screen center (640, 360 for 1280x720)
  6. Classify: on-target (<15px), horizontal lag (dx>0), horizontal lead (dx<0), vertical drift
  7. Speed-change events = dx sign reversals with |dx| > 20

Requires: ffmpeg, numpy, PIL (Pillow)
"""

import subprocess
import sys
import os
import argparse
import tempfile
import numpy as np
from PIL import Image


def convert_to_h264(video_path: str, output_dir: str) -> str:
    """Convert HEVC to H264 if the video uses HEVC codec."""
    probe = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "stream=codec_name", "-of", "csv=p=0", video_path],
        capture_output=True, text=True, timeout=10
    )
    codecs = probe.stdout.strip().split("\n")
    if "hevc" not in codecs:
        return video_path  # Already H264 or compatible

    converted = os.path.join(output_dir, "converted.mp4")
    subprocess.run(
        ["ffmpeg", "-y", "-i", video_path, "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-an", converted],
        capture_output=True, timeout=120
    )
    return converted


def extract_frames(video_path: str, output_dir: str, fps: int = 5) -> list:
    """Extract frames at the given fps. Returns sorted list of frame file paths."""
    pattern = os.path.join(output_dir, "frame_%04d.png")
    subprocess.run(
        ["ffmpeg", "-y", "-i", video_path, "-vf", f"fps={fps}", pattern],
        capture_output=True, timeout=120
    )
    frames = sorted([f for f in os.listdir(output_dir) if f.startswith("frame_") and f.endswith(".png")])
    return [os.path.join(output_dir, f) for f in frames]


def analyze_frame(img_array: np.ndarray, cx: int, cy: int, threshold: int = 40) -> dict:
    """Detect target bot and measure offset from crosshair (screen center)."""
    h, w = img_array.shape[0], img_array.shape[1]
    gray = np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140])

    # Exclude top/bottom UI (Y 200-600 on 720p)
    y_min, y_max = max(200, 0), min(600, h)
    gray_crop = gray[y_min:y_max, :]

    dark_mask = gray_crop < threshold
    if not dark_mask.any():
        return {"dx": None, "dy": None, "dist": None}

    rows_local, cols = np.where(dark_mask)
    rows = rows_local + y_min

    # Only consider dark pixels within 250px of center
    distances = np.sqrt((cols - cx) ** 2 + (rows - cy) ** 2)
    close_mask = distances < 250
    if not close_mask.any():
        return {"dx": None, "dy": None, "dist": None}

    target_x = int(np.median(cols[close_mask]))
    target_y = int(np.median(rows[close_mask]))
    dx = cx - target_x  # positive = crosshair RIGHT of target (lag)
    dy = cy - target_y  # positive = crosshair BELOW target
    dist = np.sqrt(dx ** 2 + dy ** 2)

    return {"dx": dx, "dy": dy, "dist": dist, "tx": target_x, "ty": target_y}


def classify(dx, dy, dist):
    """Classify the offset pattern."""
    if dist is None:
        return "NO_TARGET"
    if dist < 15:
        return "ON_TARGET"
    if abs(dx) > abs(dy):
        return "H_LAG" if dx > 0 else "H_LEAD"
    return "V_DOWN" if dy > 0 else "V_UP"


def main():
    parser = argparse.ArgumentParser(description="Analyze crosshair-to-target offset in a KovaaK's clip")
    parser.add_argument("video", help="Path to the video file")
    parser.add_argument("--fps", type=int, default=5, help="Frame extraction rate (default 5)")
    parser.add_argument("--threshold", type=int, default=40, help="Dark pixel threshold for target detection (default 40)")
    args = parser.parse_args()

    if not os.path.exists(args.video):
        print(f"Error: file not found: {args.video}")
        sys.exit(1)

    with tempfile.TemporaryDirectory() as tmpdir:
        # Step 1: Convert HEVC to H264 if needed
        video = convert_to_h264(args.video, tmpdir)

        # Step 2: Extract frames
        frame_paths = extract_frames(video, tmpdir, fps=args.fps)
        if not frame_paths:
            print("Error: no frames extracted")
            sys.exit(1)
        print(f"Extracted {len(frame_paths)} frames at {args.fps}fps")

        # Step 3: Analyze each frame
        cx, cy = 640, 360  # screen center for 1280x720
        results = []
        for i, fpath in enumerate(frame_paths):
            img = np.array(Image.open(fpath))
            r = analyze_frame(img, cx, cy, args.threshold)
            r["frame"] = i
            r["time"] = i / args.fps
            r["cls"] = classify(r.get("dx"), r.get("dy"), r.get("dist"))
            results.append(r)

        # Step 4: Summary
        valid = [r for r in results if r["dist"] is not None]
        if not valid:
            print("No target detected in any frame")
            sys.exit(1)

        dists = [r["dist"] for r in valid]
        dxs = [r["dx"] for r in valid]
        dys = [r["dy"] for r in valid]

        print(f"\n=== Offset (pixels) ===")
        print(f"Frames: {len(results)}, with target: {len(valid)}")
        print(f"Distance: mean={np.mean(dists):.1f}  med={np.median(dists):.1f}  std={np.std(dists):.1f}  min={np.min(dists):.1f}  max={np.max(dists):.1f}")
        print(f"X offset:  mean={np.mean(dxs):.1f}  std={np.std(dxs):.1f}  (positive = crosshair RIGHT of target = LAG)")
        print(f"Y offset:  mean={np.mean(dys):.1f}  std={np.std(dys):.1f}  (positive = crosshair BELOW target)")

        on_target = sum(1 for r in valid if r["dist"] < 15)
        h_lag = sum(1 for r in valid if r["cls"] == "H_LAG")
        h_lead = sum(1 for r in valid if r["cls"] == "H_LEAD")
        v_down = sum(1 for r in valid if r["cls"] == "V_DOWN")
        v_up = sum(1 for r in valid if r["cls"] == "V_UP")

        print(f"\n=== Classification ({len(valid)} frames) ===")
        print(f"  ON TARGET (<15px): {on_target} ({on_target/len(valid)*100:.0f}%)")
        print(f"  H-LAG:            {h_lag} ({h_lag/len(valid)*100:.0f}%)")
        print(f"  H-LEAD:           {h_lead} ({h_lead/len(valid)*100:.0f}%)")
        print(f"  V-DOWN:           {v_down} ({v_down/len(valid)*100:.0f}%)")
        print(f"  V-UP:             {v_up} ({v_up/len(valid)*100:.0f}%)")

        # Speed-change events
        sign_changes = []
        for i in range(1, len(valid)):
            dx_prev, dx_curr = valid[i-1]["dx"], valid[i]["dx"]
            if dx_prev * dx_curr < 0 and abs(dx_prev) > 20 and abs(dx_curr) > 20:
                sign_changes.append({"time": valid[i]["time"], "prev_dx": dx_prev, "curr_dx": dx_curr, "dist": valid[i]["dist"]})

        print(f"\n=== Speed-change events (dx sign reversal, |dx|>20) ===")
        print(f"Found {len(sign_changes)} events")
        for s in sign_changes:
            print(f"  t={s['time']:5.1f}s  dx: {s['prev_dx']:+5.0f} -> {s['curr_dx']:+5.0f}  dist={s['dist']:.1f}")

        # Timeline (every 2 seconds)
        print(f"\n=== Timeline (every 2s) ===")
        print(f"{'time':>6} {'dx':>6} {'dy':>6} {'dist':>6}  classification")
        for r in valid:
            if r["frame"] % (args.fps * 2) == 0:
                print(f"{r['time']:6.1f} {r['dx']:6.0f} {r['dy']:6.0f} {r['dist']:6.1f}  {r['cls']}")


if __name__ == "__main__":
    main()
