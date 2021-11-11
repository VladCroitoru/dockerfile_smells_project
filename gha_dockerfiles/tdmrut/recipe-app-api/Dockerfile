FROM python:3.9.7-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update
RUN apk add musl-dev mariadb-dev gcc
RUN pip install mysqlclient

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /scripts
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
