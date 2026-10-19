## 2026-10-19 - dynamic_ncols and colour for tqdm progress bars
**Learning:** Hardcoding `ncols` in tqdm can cause terminal truncation issues, and lack of color can reduce visual clarity for CLI progress bars.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` progress bars to prevent terminal truncation and improve visual clarity.
