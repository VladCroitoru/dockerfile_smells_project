FROM python:3.8.2-slim-buster

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y --no-install-recommends make && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false

WORKDIR /recipes

COPY pyproject.toml poetry.lock /recipes/

# Install the packages
RUN poetry install --no-dev --no-root
