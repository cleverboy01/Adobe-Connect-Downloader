## 2024-02-23 - Improve CLI progress bar UX
**Learning:** Hardcoded widths like `ncols=80` in `tqdm` progress bars can cause terminal truncation or wasted space on different setups.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` progress bars for better responsiveness and visual clarity.
