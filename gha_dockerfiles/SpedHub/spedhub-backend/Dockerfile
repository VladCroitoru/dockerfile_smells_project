FROM python:3.7-alpine

RUN apk add --no-cache --update \
    build-base \
    postgresql-dev \
    bash \
    && rm -rf /var/cache/apk/*

RUN apk add --no-cache \
    libressl-dev \
    musl-dev \
    libffi-dev && \
    pip install --no-cache-dir cryptography==2.1.4 && \
    apk del \
    libressl-dev \
    musl-dev \
    libffi-dev

RUN mkdir /app
WORKDIR  /app

COPY requirements.txt /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt