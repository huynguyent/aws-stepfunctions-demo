FROM python:3.9

WORKDIR /workdir

RUN #apt-get update -qq && apt-get -qq -y install curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH /root/.local/bin:$PATH

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction

RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash - && apt-get install -y nodejs
RUN npm install -g aws-cdk
