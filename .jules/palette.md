## 2024-05-24 - [Tqdm Progress Bar UX]
**Learning:** Hardcoded `ncols` in `tqdm` can cause terminal output truncation. Adding a color improves visibility.
**Action:** Use `dynamic_ncols=True` and `colour='green'` when initializing `tqdm` progress bars.