versions:
	which pip
	which python3

deps:
	pip install -r requirements.txt
	@pip freeze > requirements.txt

clean:
	@echo "pass"

run-dev:
	uvicorn app.main:app --reload

tests:
	pytest --version

bundle:
	rm -rf dist/
	mkdir dist
	cp -R app dist
	cp -R ./venv/lib/python3.8/site-packages/* dist
	(cd dist && zip -r lambda.zip . -x \**/__pycache__/\*)
	find ./dist ! -name 'lambda.zip' -type f -exec rm -f {} +
	find ./dist/* ! -name 'lambda.zip' -type d -exec rm -rf {} +