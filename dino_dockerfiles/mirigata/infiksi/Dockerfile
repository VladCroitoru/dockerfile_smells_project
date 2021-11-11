FROM python:3
MAINTAINER yigal@publysher.nl

WORKDIR /app/infiksi
EXPOSE 8080

RUN pip install uwsgi

ADD . /app/infiksi/

RUN pip install -e .[server]

RUN adduser --system infiksi
USER infiksi

CMD uwsgi --ini /app/infiksi/docker-uwsgi.ini
