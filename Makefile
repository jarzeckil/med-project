.PHONY: install install-poetry export-requirements clean format lint create-venv create-environment-poetry


PROJECT_NAME = med-project
PYTHON_VERSION = 3.13
PYTHON_INTERPRETER = python


help:
	@grep -E '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-30s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies using pip (Standard method)
	pip install -r requirements.txt
	pip install -e .

install-poetry: ## Install dependencies using Poetry
	poetry install

export-requirements: ## Export poetry dependencies to requirements.txt (For Maintainer)
	poetry export -f requirements.txt --output requirements.txt --without-hashes

clean: ## Delete all compiled Python files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".ruff_cache" -delete

lint: ## Lint using ruff (Check only)
	ruff format --check
	ruff check

format: ## Format source code with ruff (Fix and Format)
	ruff check --fix
	ruff format

create_venv: ## Create standard Python venv (No Poetry)
	$(PYTHON_INTERPRETER) -m venv .venv
	@echo ">>> Venv created. Activate with:"
	@echo ">>> Windows: .venv\Scripts\activate"
	@echo ">>> Linux/Mac: source .venv/bin/activate"

create_environment: ## Set up Python interpreter environment (Poetry)
	poetry env use $(PYTHON_VERSION)
	@echo ">>> Poetry environment created."