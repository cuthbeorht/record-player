versions:
	which pip
	which python3

deps:
	pip install -r requirements.txt

clean:
	@echo "pass"

run-dev:
	uvicorn app.main:app --reload