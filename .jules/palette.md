## 2024-10-02 - dynamic_ncols and colour for tqdm UX
**Learning:** Hardcoding `ncols` in `tqdm` can cause terminal output truncation. Using `dynamic_ncols=True` and setting a `colour` (like 'green') significantly improves visual clarity and responsiveness across different terminal sizes.
**Action:** Apply `dynamic_ncols=True` and `colour` parameters to all `tqdm` progress bars in CLI applications.
