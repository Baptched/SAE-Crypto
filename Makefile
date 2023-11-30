MODULES = $(filter-out */src/constantes.py, $(wildcard */src/*.py)) Défi1/tests/*.py Défi2/tests/*.py
TESTS = $(wildcard */tests/*.py)

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
	python3 -m coverage report -m ${MODULES} ${TESTS}

.PHONY: clean
clean:  
	find . -type f -name "*.pyc" | xargs rm -fr  
	find . -type d -name __pycache__ | xargs rm -fr
	find . -type d -name .mypy_cache | xargs rm -fr
	find . -type f -name .coverage | xargs rm -fr

.PHONY: verif
verif: clean typehint tests lint coverage format clean
