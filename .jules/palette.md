## 2024-05-24 - Dynamic TQDM Progress Bars
**Learning:** Hardcoding  in tqdm can lead to terminal truncation, and default colors might not provide the best visual clarity in CLI applications.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` progress bars.
