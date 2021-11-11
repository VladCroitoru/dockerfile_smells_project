FROM python:3.6-alpine

RUN apk add build-base jpeg-dev postgresql-dev zlib-dev

RUN mkdir /code
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv
RUN pipenv install --dev

ADD manage.py /code/

ADD account /code/account
ADD campaign /code/campaign
COPY reverie /code/reverie
ADD splash /code/splash
ADD templates /code/templates

ENTRYPOINT pipenv run gunicorn reverie.wsgi -b 0.0.0.0:8000
