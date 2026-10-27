## 2024-10-27 - Dynamic sizing and colour for tqdm progress bars
**Learning:** Hardcoded widths for CLI progress bars (like `ncols=80` in `tqdm`) can cause text truncation or poor display on different terminal sizes. Adding color significantly improves visual hierarchy in dense terminal output.
**Action:** Standardize on using `dynamic_ncols=True` and `colour='green'` for all `tqdm` initializations to ensure robust, responsive, and visually clear progress indicators across different user environments.
