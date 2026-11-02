## 2024-05-24 - Tqdm Progress Bar UX Pattern
**Learning:** Hardcoded width limits can cause terminal truncation, and uncolored progress bars lack visual distinction.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` progress bars, which prevents terminal truncation and improves visual clarity.
