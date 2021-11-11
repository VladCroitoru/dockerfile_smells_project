# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENV PATH=$PATH:/code/instantclient_21_3
ENV LD_LIBRARY_PATH=/code/instantclient_21_3
RUN apt update && apt install libaio1 -y