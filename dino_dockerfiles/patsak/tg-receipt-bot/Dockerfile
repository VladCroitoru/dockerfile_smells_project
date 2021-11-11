FROM python:3.6.5-alpine

RUN mkdir /app

COPY requirements.txt /app/requirements.txt

RUN apk add --update --no-cache --virtual .build-deps \
    libffi-dev \
    openssl-dev \
    gcc \
    linux-headers \
    libc-dev && \
    pip install -r/app/requirements.txt  && \
    apk del .build-deps 
    
RUN apk add --no-cache libssl1.0 

RUN adduser -D -H uwsgi

COPY *.py /app/

WORKDIR /app


