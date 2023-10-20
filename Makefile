MODULES = src/*.py tests/*.py

.PHONY: typehint
typehint:  
	mypy --ignore-missing-imports ${MODULES}

.PHONY: tests
tests:  
	python3 -m unittest -v -b tests/*.py

.PHONY: lint
lint:  
	pylint ${MODULES}

.PHONY: format
format:	
	yapf -ir ${MODULES}

.PHONY: coverage
coverage:
	python3 -m coverage run -m unittest
	python3 -m coverage report ${MODULES}

.PHONY: clean
clean:  
	find . -type f -name "*.pyc" | xargs rm -fr  
	find . -type d -name __pycache__ | xargs rm -fr

.PHONY: verif
verif: clean typehint tests lint coverage format clean