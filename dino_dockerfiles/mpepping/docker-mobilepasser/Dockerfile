FROM python:2.7-alpine

LABEL maintainer "Martijn Pepping <martijn.pepping@automiq.nl>"

RUN apk update && \
    apk add openssl && \
    wget -O mobilepasser.zip https://github.com/datr/MobilePASSER/archive/python.zip && \
    unzip mobilepasser.zip && cd MobilePASSER-python && \
    python setup.py install && \
    apk del openssl && \
    rm -rf /mobilepasser.zip /usr/lib/python*/__pycache__/*.pyc /var/cache/apk/*

entrypoint ["/MobilePASSER-python/mobilepasser/mobilepasser.py", "-c", "/mobilepasser.cfg"]

