FROM python:3.7.3-alpine

WORKDIR /usr/src/app

RUN apk update && \
    apk add build-base gcc musl-dev openssl-dev libffi-dev python3-dev && \
    apk add postgresql-dev postgresql-client libxml2-dev libxslt-dev libressl-dev musl-dev && \
    apk add jpeg-dev zlib-dev libressl-dev libjpeg


RUN python -m pip install --upgrade pip


COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .
