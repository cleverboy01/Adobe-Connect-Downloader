## 2024-05-24 - Tqdm Progress Bar Improvements
**Learning:** Hardcoded `ncols` in `tqdm` can cause terminal output truncation on varying screen sizes. Additionally, the default color might not stand out clearly.
**Action:** Implemented `dynamic_ncols=True` and `colour='green'` parameters when initializing `tqdm` instances across the application (e.g., in `progress_display.py` and `ffmpeg_progress.py`). This is a reusable UX pattern for this codebase to ensure progress bars are responsive and visually distinct.
