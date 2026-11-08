## 2026-11-08 - Responsive Progress Bars
**Learning:** Using fixed widths for CLI progress bars can lead to truncation and a poor UX on smaller terminals. The `tqdm` library supports `dynamic_ncols=True` and `colour` parameters which significantly improve responsiveness and visual clarity.
**Action:** Always prefer `dynamic_ncols=True` and a distinct color (like 'green') when initializing `tqdm` progress bars in CLI applications.
