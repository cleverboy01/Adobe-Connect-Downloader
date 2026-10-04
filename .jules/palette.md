## 2024-05-15 - Dynamic width and colors for tqdm progress bars
**Learning:** Hardcoding `ncols=80` in tqdm progress bars causes truncation on smaller terminals and limits visibility on larger ones.
**Action:** Always use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') for tqdm progress indicators in CLI applications to prevent terminal truncation and improve visual clarity.
