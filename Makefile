PROJECT_PATH=venv/
PYTHON=$(PROJECT_PATH)bin/python
PIP=$(PROJECT_PATH)bin/pip

black-all:
	black . --config black.toml

flake8:
	flake8 --config=setup.cfg

test:
	coverage run -m pytest

coverage:
	coverage report