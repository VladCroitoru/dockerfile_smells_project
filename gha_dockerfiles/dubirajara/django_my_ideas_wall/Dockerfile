FROM python:3.7-alpine

MAINTAINER dubirajara

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt

RUN apk update && apk add build-base postgresql-dev && apk add git && pip install --upgrade pip && pip install -q -r /code/requirements.txt

COPY . /code/
WORKDIR /code/

EXPOSE 8000