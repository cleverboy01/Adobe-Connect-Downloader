## 2024-05-24 - Dynamic sizing for tqdm progress bars
**Learning:** Using fixed `ncols` in tqdm can lead to terminal truncation on smaller screens, and lacks visual pop.
**Action:** Always use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') for tqdm progress indicators in this codebase to ensure responsiveness and better CLI UX.
