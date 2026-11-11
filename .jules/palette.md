## 2024-05-24 - Tqdm Progress Bar Configuration
**Learning:** Hardcoded `ncols=80` or default widths can cause terminal output truncation in specific environments.
**Action:** Use `dynamic_ncols=True` and `colour='green'` when initializing `tqdm` progress bars to prevent truncation and improve visual clarity.
