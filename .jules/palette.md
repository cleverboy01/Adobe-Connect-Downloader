## 2024-05-20 - Improved Tqdm Progress Bars
**Learning:** In CLI applications, statically sized progress bars (`ncols=80`) often truncate or break in narrow terminals.
**Action:** Adopted `dynamic_ncols=True` alongside `colour="green"` for `tqdm` initialization across the project to provide responsive, visually distinct progress feedback. This pattern should be standard for all CLI progress indicators.
