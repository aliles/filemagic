SHELL := /bin/bash

# SET UP
# install software dependencies

deps:
	pip install --upgrade --use-mirrors \
	            -r requirements/development.txt \
	            -r requirements/production.txt

# BUILD
# build and release packages

dist:
	python setup.py sdist

register:
	python setup.py register

# DOCUMENTATION
# build user documentation

site:
	cd docs; make html

docs: site

# TESTING
# unit tests, coverage testing and static type checking

coverage:
	coverage report --include="magic*"

lint:
	flake8 --exit-zero magic tests

test:
	coverage run setup.py test

unittest:
	coverage run -m unittest

# CLEAN
# remove build artifacts

clean:
	python setup.py clean --all
	find . -type f -name "*.pyc" -exec rm '{}' +
	find . -type d -name "__pycache__" -exec rmdir '{}' +
	rm -rf *.egg-info .coverage
	cd docs; make clean
