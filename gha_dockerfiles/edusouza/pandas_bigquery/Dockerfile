FROM python:3.7-alpine

MAINTAINER Eduardo Oliveira de Souza

COPY requirements.txt .

RUN apk --update add --no-cache g++

RUN pip3 install --upgrade -r requirements.txt


