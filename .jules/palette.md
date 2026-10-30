## 2024-10-30 - TQDM Dynamic Sizing and Colors
**Learning:** Hardcoded progress bar widths in CLI applications (like `ncols=80` in `tqdm`) can cause terminal truncation and visual artifacts on varied terminal sizes, leading to poor UX.
**Action:** Always use `dynamic_ncols=True` and a distinct `colour` parameter (e.g., 'green') when initializing `tqdm` progress bars in CLI tools to ensure responsive and accessible terminal output.
