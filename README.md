# Med Project

Data analysis and ML project.

## Setup

**Requirements:** Python >=3.11, Make, Poetry (optional).

### Poetry
```bash
make install-poetry
make create-environment-poetry
```

### Pip
```bash
make create-venv
source .venv/bin/activate
make install
```

## Development

### Makefile Commands
| Command | Description |
| :--- | :--- |
| `make install` | Install pip dependencies |
| `make install-poetry` | Install poetry dependencies |
| `make export-requirements` | Generate `requirements.txt` from Poetry |
| `make format` | Format code (Ruff) |
| `make lint` | Lint code (Ruff) |
| `make clean` | Remove artifacts |
| `make create_venv` | Create `.venv` |

### Code Quality
Run `make format` before committing.
Run `make lint` to check errors.

### Project Paths
Import paths from `med_project.config` to avoid hardcoding.

```python
from src.med_project.config import RAW_DATA_DIR
import pandas as pd

csv_path = RAW_DATA_DIR / "diabetes_dataset.csv"
df = pd.read_csv(csv_path)
```

### Important 
Clear notebook outputs before committing.

## Project Structure
```
├── data/              # processed/ and raw/
├── notebooks/         # Naming: <number>-<initials>-<description>
├── reports/           # Generated analysis
├── med_project/       # Source code
│   ├── config.py      # Configuration & Paths
│   ├── dataset.py     # Data scripts
│   ├── features.py    # Feature engineering
│   └── plots.py       # Visualization
├── Makefile           # Automation
├── pyproject.toml     # Config
└── requirements.txt   # Dependencies
```

## Quality checks & roadmap
- [ ] **Deps:** Sync `pyproject.toml` and `requirements.txt`.
- [ ] **Refactor:** Move logic from notebooks to `med_project/`.
- [ ] **Types:** Add type hints.
- [ ] **Tests:** Unit tests (`pytest`).
- [ ] **Clean:** Strip notebook outputs.
- [ ] **Demo:** Streamlit app.
- [ ] **MLflow:** Experiment tracking.

