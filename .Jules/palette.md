## 2024-05-24 - Dynamic sizing and color for TQDM Progress Bars
**Learning:** Hardcoded widths (like ncols=80) for progress bars cause display issues on varying terminal sizes, and default colors lack visual distinctness.
**Action:** Always use `dynamic_ncols=True` and a distinct `colour` (like 'green') when initializing `tqdm` progress bars to prevent truncation and improve visual clarity.
