FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN set -xe \
    && apt update \
    && apt upgrade

RUN pip install -U pipenv

WORKDIR /app
COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile
COPY . /app
