## 2024-05-24 - Dynamic Progress Bar Resizing
**Learning:** Terminal outputs can truncate depending on window size, and standard hardcoded columns in progress bars can look broken on smaller or larger screens. Adding visual distinctness to progress bars also improves scanning of logs.
**Action:** Used `dynamic_ncols=True` and `colour='green'` parameters when initializing `tqdm` progress bars. This is a reusable UX pattern for CLI applications to prevent terminal truncation and improve visual clarity.
