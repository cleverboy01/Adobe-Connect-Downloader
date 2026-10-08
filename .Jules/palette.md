## 2024-10-24 - [tqdm progress bar UI enhancement]
**Learning:** Using `ncols=80` hardcodes width and causes truncation/wrapping issues on terminal resize. `dynamic_ncols=True` with `colour` parameters creates a more responsive and pleasant CLI interface.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter when initializing `tqdm` progress bars to prevent truncation and improve visual clarity.
