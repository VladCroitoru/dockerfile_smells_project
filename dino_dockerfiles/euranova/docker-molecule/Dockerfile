FROM ubuntu:xenial

ENV DEVIAN_FRONTEND="noninteractive"

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python sudo bash ca-certificates python-pip && \
    apt-get clean

RUN pip install --upgrade pip && pip install ansible==2.4.2.0 molecule==2.7

WORKDIR /role

ENTRYPOINT molecule
