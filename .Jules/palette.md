## 2024-05-23 - Dynamic Progress Bars
**Learning:** Hardcoding `ncols` in tqdm progress bars can cause terminal truncation or suboptimal display.
**Action:** Always use `dynamic_ncols=True` and a `colour='green'` parameter when initializing `tqdm` to prevent truncation, ensure responsiveness, and improve visual clarity.