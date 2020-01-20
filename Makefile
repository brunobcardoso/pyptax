.PHONY: clean test

clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.pyo" -delete
	@rm -f .coverage
	@rm -rf htmlcov


test: clean
	pytest -v -rf


coverage: clean
	pytest -x --cov=pyptax/ --cov-report=term-missing --cov-report=html:htmlcov
