# 🎓 MASB Course: Hello World

Welcome to a MASB course repository. We are glad to have you here and wish you a productive and engaging learning experience.

## 🗂️ Project Structure

This practice is divided into two main sections:

- **Arduino**: All materials and instructions related to Arduino development are located in the [arduino/README.md](/arduino/README.md) file.
- **STM32Cube**: All materials and instructions related to STM32Cube development are located in the [stm32cube/README.md](/stm32cube/README.md) file.

Please refer to the respective README files for detailed guidance on each platform.

## ⚙️ GitHub Actions and Documentation Generation

This repository uses GitHub Actions to automatically generate and update documentation files. This GitHub Action must be triggered manually only once. To do so, follow these steps:

1. Click the **Actions** tab.
2. Select the workflow named **🚀 Init course**.
3. Click the **Run workflow** button (top right).
4. Make sure the branch is set to `main` and confirm by clicking **Run workflow**.

After a short wait, the workflow will complete and documentation files will be generated. Refresh the page to see the updated status badge.

**GitHub Actions Status:** [![🚀 Init course](https://github.com/{{ github_repo_fullname }}/actions/workflows/init_course.yaml/badge.svg)](https://github.com/{{ github_repo_fullname }}/actions/workflows/init_course.yaml)

> [!NOTE]
> The status badge above will not be available until the documentation generation process is finished. If the badge does not appear, please wait and refresh the page after a short period.

## 🔄 Keeping Your Fork Up to Date

If you are working from a fork of this repository, it is important to regularly synchronize your fork with the upstream repository to receive the latest updates and improvements. To update your fork:

1. Add the original repository as a remote:
   ```sh
   git remote add upstream {{ github_repo_template }}
   ```
2. Fetch the latest changes:
   ```sh
   git fetch upstream
   ```
3. Merge the changes into your local main branch:
   ```sh
   git checkout main
   git merge upstream/main
   ```
4. Push the updates to your fork:
   ```sh
   git push origin main
   ```

## 💡 Getting Help

If you encounter any difficulties or have questions regarding the course materials, please visit the course discussions forum:

[![](https://img.shields.io/badge/Go%20to%20Discussions-%E2%86%92-0366d6?style=for-the-badge&logo=github&labelColor=0366d6)](https://github.com/TheAlbertDev/MASB/discussions)

You are encouraged to participate and seek assistance from instructors and peers.

## 📝 Feedback and Issue Reporting

Your feedback is highly valuable for improving this course. If you notice any errors, inconsistencies, or have suggestions for improvement, please create an issue using the provided template:

[![](https://img.shields.io/badge/Create%20an%20Issue-%E2%86%92-28a745?style=for-the-badge&logo=github&labelColor=28a745)](https://github.com/TheAlbertDev/masb-course-hello-world/issues/new)

Thank you for helping me enhance the learning experience for everyone.

## ©️ Copyright

© 2026 Albert Álvarez-Carulla (TheAlbertDev).
