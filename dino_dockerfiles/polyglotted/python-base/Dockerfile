FROM python:2.7.11-alpine
MAINTAINER PG Developer <pgtdev@polyglotted.io>

ADD requirements.txt /tmp
RUN apk add --no-cache --virtual=base_dependencies musl-dev gcc python-dev make cmake g++ gfortran && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip install -r /tmp/requirements.txt --no-cache-dir && \
    apk del base_dependencies && \
    rm -rf /var/cache/apk/* /var/lib/apt/lists/* /tmp/* /var/tmp/*
