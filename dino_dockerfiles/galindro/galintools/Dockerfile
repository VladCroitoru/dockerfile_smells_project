FROM jfloff/alpine-python:2.7-slim

ENV PATH="${PATH}:/opt/galintools/bin"

COPY src /galintools

RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories \
    && apk update \
    && apk add --no-cache \
       g++ \
       libffi-dev \
       make \
       mongodb-tools \
       mysql-client \
       openssl \
       openssl-dev \
       openssh-client \
       python-dev \
       rsync \
       tar \
       zabbix-utils

RUN /entrypoint.sh -P /galintools/requirements.txt

ADD https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.6.tar.gz /tmp/

RUN cd /tmp \
    && tar -zxpf mysql-connector-python-2.1.6.tar.gz \
    && cd mysql-connector-python-2.1.6 \
    && pip install --egg . \
    && cd /galintools \
    && ./setup.py build \
    && ./setup.py install --force \
    && cd / \
    && rm -rf /galintools \
    && apk del \
       g++ \
       libffi-dev \
       make \
       openssl \
       openssl-dev \
       python-dev \
       tar \
    && rm -rf /tmp/* /root/.cache/*

WORKDIR "/opt/galintools/bin"

