## 2024-03-24 - Improve Terminal Progress Bar UX
**Learning:** Hardcoding `ncols=80` in tqdm progress bars can lead to truncation and poor visual experience in smaller terminals.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` progress bars, which prevents terminal truncation and improves visual clarity.
