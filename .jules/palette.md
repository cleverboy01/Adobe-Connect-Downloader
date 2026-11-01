## 2024-05-24 - Dynamic Width and Color for Progress Bars
**Learning:** Hardcoded `ncols=80` in `tqdm` can cause terminal truncation. Using `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') prevents truncation and improves visual clarity.
**Action:** Use `dynamic_ncols=True` and `colour='green'` when initializing `tqdm` progress bars in CLI tools.