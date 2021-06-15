.ONESHELL:

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

run:
	. venv/bin/activate; \
	  python top_commented_articles.py -r $(number_of_results)

help:
	python top_commented_articles.py -h

test:
	python -m unittest test

coverage:  ## Run tests with coverage
	coverage erase
	coverage run --source='.' -m unittest test
	coverage report -m

test:

