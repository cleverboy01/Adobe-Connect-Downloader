## 2024-05-14 - Tqdm Progress Bar UX
**Learning:** Hardcoding `ncols` for tqdm progress bars leads to terminal truncation issues on varying screen sizes. A reusable UX pattern for this codebase is to use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` to prevent truncation and improve visual clarity.
**Action:** Always use `dynamic_ncols=True` and `colour='green'` for `tqdm` bars instead of hardcoding `ncols`.
