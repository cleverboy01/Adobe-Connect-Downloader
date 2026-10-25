## 2024-05-24 - Tqdm Dynamic Sizing and Color
**Learning:** Hardcoded `ncols` in `tqdm` progress bars can cause terminal truncation or poor display on different terminal sizes. Adding color improves visual hierarchy and user feedback in CLI applications without full UIs.
**Action:** Always use `dynamic_ncols=True` and `colour='green'` (or another appropriate color) when initializing `tqdm` bars for better responsiveness and visibility.
