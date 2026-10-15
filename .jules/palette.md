## 2024-05-24 - Dynamic tqdm Sizing and Coloring
**Learning:** Hardcoded width (e.g., `ncols=80`) and plain text progress bars can cause terminal truncation and lack visual hierarchy in CLI apps.
**Action:** Use `dynamic_ncols=True` and `colour='green'` when initializing `tqdm` progress bars to adapt to terminal size and improve visual clarity, which is a reusable UX pattern for this design system.
