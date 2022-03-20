help:
	@echo MAKE Application values
	@echo
	@echo "versions:		Displays the versions of the PIP and Python3 being used"
	@echo "deps: 			Install and freeze application requirements"
	@echo "clean:			Cleans up cache files. **NOT CURRENTLY USED**"
	@echo "run-dev:		Runs the application locally using uvicorn on default host and ports"
	@echo "test-unit:		Run unit tests found in ./tests"
	@echo "bundle: 		Create bundlw to AWS Lambda **TO BE DEPRECATED**"
	@echo "			Bundle has become to large to deploy directly to AWS Lambda"
	@echo "lint:			Lint the code"

versions:
	pip --version
	python3 --version

deps:
	pip install -r requirements.txt
	@pip freeze > requirements.txt

clean:
	@echo "pass"

run-dev:
	uvicorn app.main:app --reload

test-unit:
	pytest ./tests

bundle:
	rm -rf dist/
	mkdir dist
	cp -R app dist
	cp -R ./venv/lib/python3.8/site-packages/* dist
	(cd dist && zip -r lambda.zip . -x \**/__pycache__/\*)
	find ./dist ! -name 'lambda.zip' -type f -exec rm -f {} +
	find ./dist/* ! -name 'lambda.zip' -type d -exec rm -rf {} +

lint:
	@echo Linting files
	@autopep8 --recursive --in-place ./app ./tests

db-upgrade:
	@echo Upgrading configured database to HEAD
	@alembic upgrade head

db-downgrade:
	@echo Downgrading configured database to BASE
	@alembic downgrade base
