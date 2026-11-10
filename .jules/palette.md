## 2024-05-18 - Dynamic Terminal Progress Bars
**Learning:** Using `ncols=80` for tqdm progress bars in CLI applications can cause truncation or layout issues on different terminal sizes. A better reusable UX pattern is to use `dynamic_ncols=True` alongside a `colour` parameter (like 'green') for better visual clarity and responsiveness.
**Action:** Update `tqdm` initializations in `progress_display.py` and `ffmpeg_progress.py` to use `dynamic_ncols=True` and `colour='green'`.
