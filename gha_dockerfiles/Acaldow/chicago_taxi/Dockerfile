# syntax=docker/dockerfile:1

FROM amazoncorretto:8

RUN yum -y update

RUN yum -y install python3.8 python3-dev python3-pip
RUN python3 --version

ENV PYSPARK_DRIVER_PYTHON python3
ENV PYSPARK_PYTHON python3

RUN pip3 install --upgrade pip
RUN pip3 install pytest

RUN pip3 install py4j
RUN pip3 install pyspark

WORKDIR /app
COPY chicagotaxi /app/chicagotaxi
COPY tests /app/tests