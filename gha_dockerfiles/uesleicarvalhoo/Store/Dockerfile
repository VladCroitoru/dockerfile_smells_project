FROM python:3.9-slim-buster

WORKDIR /app

RUN apt update -y && apt upgrade -y && apt install -y make apt-utils && pip install --upgrade pip

RUN pip install poetry

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone

ADD pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev --no-interaction --no-ansi

ADD . .
