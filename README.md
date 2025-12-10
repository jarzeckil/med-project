# Med Project

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Group project for data analysis and exploration project.

## 📋 Requirements

* **Python >=3.11**
* **Make** (optional, but recommended for running commands)


## 🚀 Installation & Setup

Choose the installation method that fits your workflow.

### Option A: Poetry

If you have [Poetry](https://python-poetry.org/) installed and want to manage dependencies actively:

1.  **Install dependencies:**
    ```bash
    make install-poetry
    ```
2.  **Activate the shell:**
    ```bash
    make create-environment-poetry
    ```

### Option B: Standard pip

If you want a standard installation using `pip` and `requirements.txt`:

1.  **Create a virtual environment:**
    ```bash
    make create-venv
    ```

2.  **Activate the environment:**

3.  **Install dependencies:**
    ```bash
    make install
    ```

---

## 🧹 Code Quality (Ruff)

This project uses **[Ruff](https://github.com/astral-sh/ruff)** for both linting and formatting. It ensures our code style is consistent across the team.

Before committing your code, please run:

```bash
make format
```

This command will:
- Fix import sorting.
- Format code (indentation, spacing).
- Auto-fix common syntax issues.

To check for errors without modifying files, run:
```bash
make lint
```

## 🧭 Project paths (from `med_project.config`)

This project centralizes important directories in `med_project/config.py` using `pathlib.Path`. You should **always import and reuse these constants** instead of hard‑coding paths.

### How to use these paths in your code

Example – loading the raw diabetes dataset:

```python
from med_project.config import RAW_DATA_DIR
import pandas as pd

csv_path = RAW_DATA_DIR / "diabetes_dataset.csv"
df = pd.read_csv(csv_path)
```

If needed, create your own constants.

## ❗ Important
Remember to clear jupyter notebook outputs before commiting!

## 🛠️ Makefile Shortcuts

We use a `Makefile` to automate common tasks. You can run these commands from the project root:

| Command | Description |
| :--- | :--- |
| `make install` | Installs dependencies from `requirements.txt` (for pip users). |
| `make install-poetry` | Installs dependencies from `pyproject.toml` (for Poetry users). |
| `make export-requirements` | Generates `requirements.txt` from Poetry (run this after adding new libs). |
| `make format` | Formats code and fixes imports using **Ruff**. |
| `make lint` | Checks code quality without modifying files. |
| `make clean` | Removes `__pycache__` and other temporary artifacts. |
| `make create_venv` | Creates a standard `.venv` folder (if you don't want to do it manually). |


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
││
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         med_project and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
││
└── med_project   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes med_project a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```


## ✅ Project Roadmap & Quality Checklist

### 🏗️ Infrastructure & Automation (CI/CD)
- [ ] **GitHub Actions:** Create `.github/workflows/ci.yml` to automatically run `make lint` on every Pull Request.
- [ ] **Dependency Sync:** Ensure `pyproject.toml` and `requirements.txt` are always synchronized (run `make export-requirements`).

### 💎 Code Quality & Engineering
- [ ] **Refactoring:** Move reusable logic from Notebooks (`notebooks/`) to the Python package (`med_project/`).
- [ ] **Type Hinting:** Add type hints to all functions in `med_project` (e.g., `def clean(df: pd.DataFrame) -> pd.DataFrame:`).
- [ ] **Unit Tests:** Implement basic tests using `pytest` for critical data processing functions (create a `tests/` directory).

### 📢 Documentation & Business Context
- [ ] **Problem Statement:** Add a section at the top of README explaining the specific medical problem we are solving.
- [ ] **Business Value:** Define how this model helps (e.g., "reduces diagnosis time", "minimizes false negatives").
- [ ] **Clean Notebooks:** Ensure "Gold Standard" notebooks are readable and stripped of outputs before committing.

### 🚀 Deployment & Extras
- [ ] **Interactive Demo:** Create a simple **Streamlit** app (`app.py`) to showcase the model functionality.
- [ ] **Experiment Tracking:** (Optional) Use **MLflow** to log model parameters and performance metrics instead of printing them.
