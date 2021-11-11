FROM python:3.6.1-slim

MAINTAINER joway wang <joway.w@gmail.com>

RUN apt update \
    && apt install -y build-essential libmysqlclient-dev mysql-client nginx libpcre3 libpcre3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code/cache
WORKDIR /code
