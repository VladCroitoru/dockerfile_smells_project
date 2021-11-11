FROM python:3.5-slim

MAINTAINER Gilles Ameri

ENV LANG             fr

RUN mkdir -p /usr/spacy
COPY . /usr/spacy/

RUN apt-get update
RUN apt-get install -y build-essential python-dev git

RUN pip install --upgrade pip setuptools

RUN pip install -U spacy
RUN python -m spacy download ${LANG}

WORKDIR /usr/spacy

CMD ["python"]
