# The Python Mega Course — Portfolio & Project Tracker

> Build along with Udemy’s **[The Python Mega Course](https://www.udemy.com/course/the-python-mega-course/)** and turn it into a **job‑ready GitHub portfolio**.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12+-blue"/>
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green"/>
  <img alt="CI" src="https://img.shields.io/github/actions/workflow/status/murray-milton/python-mega-course/ci.yml?label=CI"/>
  <img alt="Code style: Black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/>
  <img alt="Linter: Ruff" src="https://img.shields.io/badge/linter-ruff-ffc107"/>
</p>

## 🎯 Why this repo exists

This repo documents my progress through the course and presents **production‑quality projects** recruiters can quickly assess. Every project ships with:

* Clear README and screenshots
* Tests (`pytest`) and quality gates (Ruff + Black)
* Reproducible env (`.venv` + `requirements.txt` or `pyproject.toml`)
* CI on GitHub Actions

## 🧭 Quick start

```bash
# 1) Clone
git clone git@github.com:murray-milton/python-mega-course.git
cd python-mega-course

# 2) Create & activate a local venv
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 3) Install dev tooling
pip install -U pip
pip install -r requirements-dev.txt  # or: pip install -e .[dev]

# 4) Run quality checks
ruff check . && black --check . && pytest -q
```

## 🧱 Repo structure

```
python-mega-course/
├─ .github/workflows/ci.yml          # CI: lint + test
├─ .pre-commit-config.yaml           # local hooks
├─ requirements.txt                  # runtime deps (per project)
├─ requirements-dev.txt              # ruff, black, pytest, etc.
├─ pyproject.toml                    # optional: tool configs
├─ PROJECTS.md                       # project checklist & notes
├─ src/
│  └─ <project_slug>/                # each app lives in its folder
├─ tests/
│  └─ <project_slug>/                # matching tests
├─ assets/                           # screenshots / gifs
└─ README.md
```

## 🗂️ Project index (live demos & status)

> Tick the boxes as you complete modules. Provide a 1‑line value statement for each.

| #  | Project                       | Area          | Demo | Status         | Highlight                    |
| -- | ----------------------------- | ------------- | ---- | -------------- | ---------------------------- |
| 01 | Temperature Converter (CLI)   | Python Basics | —    | ◻︎ Not started | Arg parsing, unit tests      |
| 02 | Expense Tracker (CSV→Pandas)  | Data          | —    | ◻︎             | ETL, data validation         |
| 03 | Web Scraper (Requests+BS4)    | Web           | —    | ◻︎             | Robust selectors, throttling |
| 04 | Weather Dashboard (Streamlit) | Data Viz      | —    | ◻︎             | API keys & caching           |
| 05 | GUI Todo (Tkinter)            | Desktop       | —    | ◻︎             | Packaging as exe/app         |
| 06 | URL Shortener (Flask)         | Web           | —    | ◻︎             | Blueprints, SQLite           |
| 07 | Image Processor (Pillow)      | Imaging       | —    | ◻︎             | Batch ops                    |
| 08 | PDF Toolbox (PyPDF)           | Docs          | —    | ◻︎             | Merge/split/ocr              |
| 09 | Portfolio Optimizer (NumPy)   | DS            | —    | ◻︎             | Unit-tested math             |
| 10 | AI Assistant (LangChain)      | AI            | —    | ◻︎             | Tool use & prompts           |

> Note: The official curriculum includes **~20 real‑world apps** (web, data, desktop GUIs, scraping, etc.). I mirror them here and may adapt scope to be portfolio‑ready.

## 🧪 Quality

* **Linting:** Ruff (`ruff check .`)
* **Formatting:** Black (`black .`)
* **Testing:** Pytest (`pytest -q`)
* **Pre-commit:** run checks before each commit

```yaml
# .pre-commit-config.yaml (excerpt)
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
        args: ["--fix"]
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
```

## 🚦 CI (GitHub Actions)

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
  pull_request:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -m pip install -U pip
      - run: pip install -r requirements-dev.txt
      - run: ruff check .
      - run: black --check .
      - run: pytest -q
```

## 🛠️ Local dev

* Create a project folder under `src/<project_slug>` and matching tests in `tests/<project_slug>`
* Add runtime deps to `requirements.txt` (pin versions) or a per‑project `requirements-<slug>.txt`
* Add a minimal `README.md` inside each project folder with screenshots

## 📸 Screenshots

Place images in `assets/` and reference them like:

```markdown
![Weather Dashboard](assets/weather_dashboard.png)
```

## 🧾 License

MIT — see [LICENSE](LICENSE)

## 👋 Contact

**Murray Milton** — [murray-milton](https://github.com/murray-milton) — [murraylmilton@outlook.com](mailto:miltonmln357@gmail.com.com)

---

### Recruiter TL;DR

* Practical, deployed Python apps (web/data/desktop)
* Clean code with tests and automated checks
* Each folder is a real, runnable project you can scan in minutes
