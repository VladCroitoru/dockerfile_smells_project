FROM python:3.4.5

MAINTAINER William Gibb <william.gibb@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran

RUN mkdir -p /opt/pandas/build/

COPY requirements.txt /opt/pandas/build/requirements.txt

RUN pip install -r /opt/pandas/build/requirements.txt
