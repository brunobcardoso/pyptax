.PHONY: clean clean_build test coverage docs publish_test publish_prod

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

docs:
	sphinx-build docs docs/_build

publish_test:
	poetry publish -r testpypi --build

publish_prod:
	poetry publish --build
