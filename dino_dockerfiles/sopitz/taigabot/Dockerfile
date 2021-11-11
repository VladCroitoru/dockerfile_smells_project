FROM python:3.6.0-alpine

MAINTAINER sopitz <simon.opitz@luminoso-consulting.de>

RUN apk update && apk add git gcc alpine-sdk bash

RUN pip install slackclient
RUN pip install git+https://github.com/sopitz/python-taiga.git

ADD bot /bot

WORKDIR /bot

CMD python taigabot.py
