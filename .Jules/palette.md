## 2024-10-21 - Dynamic tqdm Progress Bars
**Learning:** Hardcoded `ncols` in `tqdm` progress bars can cause terminal truncation or poor visual experience on differently sized terminals.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` to prevent truncation and improve visual clarity, making it a reusable UX pattern for CLI progress bars.
