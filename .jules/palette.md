## 2024-05-24 - Dynamic tqdm Sizing and Coloring
**Learning:** Using hardcoded `ncols=80` for `tqdm` progress bars can truncate terminal output on smaller screens and looks unoptimized on larger screens. Additionally, adding color improves visual clarity.
**Action:** A reusable UX pattern for this codebase is to use `dynamic_ncols=True` and `colour='green'` when initializing `tqdm` progress bars.
