FROM python:3
MAINTAINER belak@coded.io

RUN mkdir -p /opt/seabird
WORKDIR /opt/seabird

COPY requirements.txt /opt/seabird
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2

COPY . /opt/seabird

ENV PYTHONUNBUFFERED true
