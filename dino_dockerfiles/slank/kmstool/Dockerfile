FROM alpine:latest

ADD . /code
RUN apk update \
    && apk add \
        python \
        py-pip \
        python-dev \
        gcc \
        libc-dev \
        libgcc \
    && pip install /code \
    && apk del \
        python-dev \
        gcc \
        libc-dev \
        libgcc \
    && rm -rf /var/cache/apk/*
