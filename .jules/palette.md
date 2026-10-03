## 2024-05-16 - Prevent terminal output truncation and improve tqdm visual clarity
**Learning:** Hardcoding `ncols` in `tqdm` can cause truncation on smaller terminals, and default colors might not stand out.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` progress bars to prevent truncation and improve visibility.
