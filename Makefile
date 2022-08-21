
help:
	@echo "test:         test"
	@echo "publish_test: publish to test registry"
	@echo "publish:      publish to stable registry"

.PHONY: build
build: clean
	python3 -m build -s -w -n

.PHONY: test-with-cov
test-with-cov:
	 PYTHONPATH=$(shell pwd)/src py.test --cov pypinyin_g2pw tests src/pypinyin_g2pw -v

.PHONY: test
test:
	PYTHONPATH=$(shell pwd)/src py.test tests src/pypinyin_g2pw -v

.PHONY: publish
publish: build
	@echo "publish to pypi"
	twine upload dist/*

.PHONY: publish_test
publish_test: build
	@echo "publish to test pypi"
	twine upload --repository test dist/*

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -rf .cache/
	rm -rf .pytest_cache/
	rm -fr htmlcov/
