SHELL := /bin/bash

# SET UP
# install software dependencies

deps:
	pip install --upgrade \
	            -r requirements/development.txt \
	            -r requirements/production.txt

# BUILD
# build and release packages

build:
	python setup.py sdist
	python setup.py bdist_wheel

register:
	python setup.py register

upload:
	python setup.py sdist upload
	python setup.py bdist_wheel upload

# DOCUMENTATION
# build user documentation

site:
	cd docs; make html

docs: site

# TESTING
# unit tests, coverage testing and static type checking

coverage:
	coverage report --show-missing

lint:
	flake8 --exit-zero magic tests

test:
	coverage run setup.py test

unittest:
	coverage run -m unittest discover

# CLEAN
# remove build artifacts

clean:
	python setup.py clean --all
	find . -type f -name "*.pyc" -exec rm '{}' +
	find . -type d -name "__pycache__" -exec rmdir '{}' +
	rm -rf *.egg-info .coverage
	cd docs; make clean
