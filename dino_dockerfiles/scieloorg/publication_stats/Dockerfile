FROM python:3.5.2

MAINTAINER tecnologia@scielo.org

COPY . /app
COPY production.ini-TEMPLATE /app/config.ini

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn

ENV PUBLICATIONSTATS_SETTINGS_FILE=/app/config.ini

RUN python setup.py install
