# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev && \
    python -m dostoevsky download fasttext-social-network-model

COPY service ./service

CMD ["python", "-m", "service"]
