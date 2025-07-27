# Internal README – Website Repository

This repository contains the source files for our project website, built with [Jekyll](https://jekyllrb.com/) using the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme. The site is hosted via GitHub Pages and is meant to support our teaching efforts in machine learning for interdisciplinary audiences.

This README explains the structure of the repository and how to update or extend the content.

---

## 🗂 Repository structure

```text
_config.yml                  # Global configuration for Jekyll and theme settings
_data/navigation.yml         # Defines the site's navigation bar structure
_includes/head/custom.html   # Custom additions to the HTML <head> (e.g., metadata, tracking)
_pages/                      # Main content pages (see below)
assets/                      # Images and site icons
  ├── img/                   # Project images (e.g., logo)
  └── favicon/               # Files related to the site favicon (browser tab icon)
CNAME                        # Custom domain configuration for GitHub Pages
Gemfile                      # Ruby dependencies (Jekyll and theme)
LICENSE                      # Project license
```

### `_pages/`

This folder contains the primary content pages. The structure here is representative of how to set up materials for a specific teaching project.

```text
_pages/
├── index.md                 # Landing page for the site
└── banz-2025/               # Example subdirectory for a specific teaching project
    ├── overview.md          # General overview of the course
    ├── societal.md          # Notes on societal/ethical context of ML
    └── technical.md         # Technical notes and explanations for ML concepts
```

To add another course or project, replicate the structure inside `banz-2025/` with appropriate Markdown files, update the navigation in `_data/navigation.yml`, and ensure that permalinks are set within each Markdown file.

---

## 🧪 Local development

To preview changes locally before pushing:

1. Install Ruby (e.g., via `rbenv`, `rvm`, or your package manager)
2. Install the necessary gems:

'bash
bundle install
'

3. Serve the website locally:

'bash
bundle exec jekyll serve
'

4. Open your browser at [http://localhost:4000](http://localhost:4000)

This will let you test the website and check formatting live as you edit content.

---

## 🛠 Editing content

- All course content is in `_pages/`, grouped by project or course name.
- To change the navigation bar, update `_data/navigation.yml`.
- To add custom HTML or metadata, modify `_includes/head/custom.html`.

Please do not edit the `assets/favicon/` folder unless you are changing the site icon set.

---

## 🔗 Resources

- [Jekyll documentation](https://jekyllrb.com/docs/)
- [Minimal Mistakes documentation](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)
