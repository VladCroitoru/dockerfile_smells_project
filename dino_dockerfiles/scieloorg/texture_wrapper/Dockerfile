FROM python:3.5

MAINTAINER tecnologia@scielo.org

COPY . /app
COPY production.ini-TEMPLATE /app/config.ini

RUN pip install --upgrade pip
RUN chmod -R 755 /app/*

WORKDIR /app

RUN python setup.py install