FROM python:2.7.12

MAINTAINER tecnologia@scielo.org

RUN apt-get update
RUN apt-get install -y lib32z1
RUN apt-get install -y lib32ncurses5

COPY requirements.txt /app/requirements.txt 

WORKDIR /app

RUN pip install -r /app/requirements.txt