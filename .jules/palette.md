## 2024-05-24 - Dynamic TQDM Progress Bars
**Learning:** Hardcoding `ncols=80` in tqdm progress bars causes terminal truncation on smaller screens, while lacking color makes it visually blend into standard CLI output.
**Action:** Use `dynamic_ncols=True` and `colour='green'` as a reusable UX pattern for all tqdm instances in this codebase to ensure responsiveness and visual clarity.
