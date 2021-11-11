# Super Simple Docker File

from ubuntu:latest
MAINTAINER Don Johnson "dj@codetestcode.io"

RUN apt-get  -qq update --fix-missing

RUN apt-get -qq install python-dev python python-virtualenv python-pip --assume-yes

add service/ /service/

RUN mkdir -p /venv/
RUN virtualenv /venv/

RUN /venv/bin/pip install -r requirements.txt
EXPOSE 80

CMD cd /service/ && /venv/bin/python server.py
