## 2024-05-24 - Tqdm Progress Bar Configuration
**Learning:** Hardcoding `ncols=80` or omitting sizing constraints for `tqdm` progress bars can lead to terminal truncation on smaller/resized screens, resulting in poor CLI UX. Furthermore, progress bars without colors might lack clarity and distinction from other terminal text.
**Action:** Always utilize `dynamic_ncols=True` and a `colour` parameter (e.g., 'green') when initializing `tqdm` to prevent terminal truncation and improve visual clarity.
