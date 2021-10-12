DOCKER_IMAGE_NAME = aws-stepfunctions-demo

python_dirs = functions stack app.py

ifneq ($(wildcard ~/.aws),)
	DOCKER_AWS_OPTS=-v $(HOME)/.aws:/root/.aws
else
	DOCKER_AWS_OPTS=
endif

DOCKER=docker run --user root -it --rm $(DOCKER_AWS_OPTS) \
	-w /workdir \
	-e AWS_DEFAULT_REGION=ap-southeast-2 \
	$(DOCKER_IMAGE_NAME)

docker-build:
	docker build --tag $(DOCKER_IMAGE_NAME) .

format:
	poetry run black $(python_dirs)
	poetry run isort $(python_dirs)

init:
	poetry install

test:
	poetry run black --check $(python_dirs)
	poetry run isort --check-only $(python_dirs)
	poetry run mypy $(python_dirs)

docker-test: docker-build
	$(DEPLOY_DOCKER) bash -euo pipefail -c 'make test'

deploy:
# https://github.com/aws/aws-cdk/issues/14658
	@echo "--- Deploying AWS resources"
	NPM_CONFIG_UNSAFE_PERM=true npx cdk deploy --all --require-approval never

docker-deploy: docker-build
	$(DEPLOY_DOCKER) bash -euo pipefail -c 'make deploy'
