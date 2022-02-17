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
	@autopep8 --recursive --in-place ./app

db-upgrade:
	@echo Upgrading configured database to HEAD
	@alembic upgrade head

db-downgrade:
	@echo Downgrading configured database to BASE
	@alembic downgrade base

terraform-validate:
	@echo "Validating Terraform"
	@terraform -chdir=terraform validate

terraform-format: terraform-validate
	@echo "Formatting Terraform files"
	@terraform -chdir=terraform fmt


terraform: terraform-format
	@echo Running Terraform

aws-deploy: terraform
	@echo "Deploying Terraform to AWS Account"
	@terraform -chdir=terraform apply

aws-undeploy:
	@echo "Undeploy AWS"
	@terraform -chdir=terraform destroy