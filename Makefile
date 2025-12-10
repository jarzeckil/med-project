#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = med-project
PYTHON_VERSION = 3.13
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install dependencies using pip (Standard method)
.PHONY: install
install:
	pip install -r requirements.txt
	pip install -e .

## Install dependencies using Poetry
.PHONY: install-poetry
install-poetry:
	poetry lock
	poetry install

## Export poetry dependencies to requirements.txt (For Maintainer)
.PHONY: export-requirements
export-requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".ruff_cache" -delete

## Lint using ruff (Check only)
.PHONY: lint
lint:
	ruff format --check
	ruff check

## Format source code with ruff (Fix and Format)
.PHONY: format
format:
	ruff check --fix
	ruff format

## Create standard Python venv (No Poetry)
.PHONY: create-venv
create_venv:
	$(PYTHON_INTERPRETER) -m venv .venv
	@echo ">>> Venv created. Activate with:"
	@echo ">>> Windows: .venv\Scripts\activate"
	@echo ">>> Linux/Mac: source .venv/bin/activate"

## Set up Python interpreter environment (Poetry)
.PHONY: create-environment-poetry
create_environment:
	poetry env use $(PYTHON_VERSION)
	@echo ">>> Poetry environment created."

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)