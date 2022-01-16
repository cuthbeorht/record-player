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
	cp -R app/* dist
	(cd dist && zip -r lambda.zip app -x \*/__pycache__/\*)
	(cd dist && zip -r lambda.zip  ../venv/lib/python3.8/site-packages -x \*/__pycache__/\*)
