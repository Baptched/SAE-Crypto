MODULES = $(filter-out defi1/src/constantes.py, $(wildcard */src/*.py)) defi1/tests_defi1/*.py defi2/tests_defi2/*.py
TESTS = $(wildcard */tests_*/*.py)

.PHONY: typehint
typehint:  
	mypy --ignore-missing-imports ${MODULES}

.PHONY: tests
tests:  
	python3 -m unittest -v -b ${TESTS}

.PHONY: lint
lint:  
	pylint ${MODULES}

.PHONY: format
format:	
	yapf -ir ${MODULES}

.PHONY: coverage
coverage:
	python3 -m coverage run -m unittest -v -b ${TESTS}
	python3 -m coverage report -m ${MODULES} 

.PHONY: clean
clean:  
	find . -type f -name "*.pyc" | xargs rm -fr  
	find . -type d -name __pycache__ | xargs rm -fr
	find . -type d -name .mypy_cache | xargs rm -fr
	find . -type f -name .coverage | xargs rm -fr

.PHONY: verif
verif: clean typehint lint coverage format clean
