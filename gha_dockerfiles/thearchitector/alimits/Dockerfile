# syntax=docker/dockerfile:1.2


FROM python:3.7-slim-buster

## setup user and install system packages
RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y neovim curl procps && \
    apt-get autoremove --purge && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip

WORKDIR /root/alimits

## configure poetry settings
ENV POETRY_NO_INTERACTION=1 \
    POETRY_NO_ANSI=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    PATH="/root/.poetry/bin:${PATH}"

## install poetry
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

## copy and install project dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-root --remove-untracked

## copy everything else
COPY . ./
RUN poetry install

CMD [ "pytest", "tests" ]