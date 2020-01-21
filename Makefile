.PHONY: clean clean_build test coverage

clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.pyo" -delete
	@rm -f .coverage
	@rm -rf htmlcov

clean_build:
	@rm -rf build dist .egg pyptax.egg-info

test: clean
	pytest -v -rf

coverage: clean
	pytest -x --cov=pyptax/ --cov-report=term-missing --cov-report=html:htmlcov

publish_test: clean_build
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/*

publish_prod: clean_build
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
