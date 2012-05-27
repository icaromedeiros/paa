clean:
	@find . -name "*.pyc" -delete

test: clean
	@echo "Running all tests..."
	@nosetests -s --with-coverage --tests=tests --with-xunit
