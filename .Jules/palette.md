## 2026-10-09 - TQDM Terminal Truncation Fix
**Learning:** Hardcoded `ncols` in `tqdm` progress bars or missing `dynamic_ncols` causes truncation in smaller terminal windows, leading to a degraded CLI experience. Additionally, color coding improves visual clarity for standard output progress.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` progress bars to prevent terminal truncation and improve visual clarity.
