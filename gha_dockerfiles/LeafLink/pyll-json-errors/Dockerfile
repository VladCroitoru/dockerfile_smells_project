FROM python:3.6-alpine

RUN apk update && \
    apk add make \
            curl \
            gcc \
            musl-dev

# Setup Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_VERSION=1.0.5 python3
ENV PATH ${PATH}:/root/.poetry/bin
RUN poetry config virtualenvs.create false

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Add all code
COPY ./ .

# Install deps
RUN poetry install -E all

EXPOSE 5001

ENTRYPOINT [ "make", "docs-serve" ]
