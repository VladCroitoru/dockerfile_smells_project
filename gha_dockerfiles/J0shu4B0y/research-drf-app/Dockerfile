FROM python:3.8-alpine
MAINTAINER Max Khrichtchatyi

ENV PYTHONBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
WORKDIR /app
COPY ./app/ /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D app
RUN chown -R app:app /vol/
RUN chmod -R 755 /vol/web
USER app
