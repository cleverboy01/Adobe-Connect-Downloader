## 2024-05-18 - Responsive and Colorful CLI Progress Bars
**Learning:** Hardcoding `ncols` in `tqdm` progress bars can cause visual issues or truncate information depending on the user's terminal window size. Also, using colors can add a nice touch to CLI output without adding complexity.
**Action:** Always use `dynamic_ncols=True` and a `colour` parameter (like `'green'`) for `tqdm` progress bars in CLI tools to ensure they adapt to any screen size and feel polished.
