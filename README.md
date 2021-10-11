# AWS StepFunctions Demo

Demo for AWS StepFunctions deployed through CDK

## Prerequisites
* [Poetry](https://python-poetry.org/docs/master/#installation)
* Python 3.9. [Installing through pyenv](https://github.com/pyenv/pyenv) is recommended
* [NodeJs](https://nodejs.org/en/)
* [AWS CDK CLI](https://docs.aws.amazon.com/cdk/latest/guide/cli.html)
* [Docker](https://docs.docker.com/get-docker/)

## Development
### Set up project
```bash
make init
```
### Test
Run test in local machine 
```bash
make test
```

Run test in Docker
```bash
make docker-test
```

### Deploy
Deploy in local machine 
```bash
make test
```

Deploy test in Docker
```bash
make docker-test
```
