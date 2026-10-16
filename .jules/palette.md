## 2024-05-18 - Tqdm Dynamic Sizing
**Learning:** Hardcoding `ncols=80` in tqdm progress bars can cause terminal truncation or wasted space on different screen sizes.
**Action:** Always use `dynamic_ncols=True` and a `colour` parameter (e.g., "green") when initializing `tqdm` progress bars in CLI applications to ensure the bar adapts to the terminal width and improves visual clarity.
