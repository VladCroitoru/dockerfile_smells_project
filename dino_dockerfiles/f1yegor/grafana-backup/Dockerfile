FROM docker.io/pandada8/alpine-python:3-tiny
MAINTAINER f1yegor

ADD . /app
WORKDIR /app
RUN chmod a+x aws-backup.sh

RUN pip3 install --upgrade pip
RUN pip3 install --egg -r requirements.txt
RUN pip3 install grafcli awscli

VOLUME ["/db"]

ENTRYPOINT ["/app/aws-backup.sh"]

