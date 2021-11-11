FROM python:3.6-alpine
MAINTAINER pnsn@uw.edu

ENV PYTHONUNBUFFERED 1
COPY ./requirements/ /requirements/

RUN apk add --update --no-cache postgresql-libs jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
    
RUN pip install -r /requirements/local.txt

RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user

USER user
