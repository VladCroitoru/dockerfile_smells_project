FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /auctioncars

RUN apt-get update

COPY requirements.txt /auctioncars/
RUN pip install -r requirements.txt

COPY . /auctioncars/
