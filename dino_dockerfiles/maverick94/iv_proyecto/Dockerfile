FROM python:3

MAINTAINER Andrés J. Gallardo

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD gunicorn API_web:__hug_wsgi__
