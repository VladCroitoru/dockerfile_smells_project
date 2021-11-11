FROM python:3.5.2

MAINTAINER tecnologia@scielo.org

RUN apt-get update && apt-get install -y libmemcached-dev

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn

RUN python setup.py install