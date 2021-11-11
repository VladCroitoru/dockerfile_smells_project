FROM alpine:latest

MAINTAINER Patrick Pokatilo <docker-hub@shyxormz.net>

ENV LANG C

RUN apk update --no-progress && \
    apk add --no-cache --no-progress \
        py-pip \
        git \
        mercurial && \
    pip install 'requests>=2.8.1'

ADD scripts /opt/resource
