FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

COPY requirements.txt /backend/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /backend/