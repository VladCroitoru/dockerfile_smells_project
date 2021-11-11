FROM python:2.7-slim

MAINTAINER confirm IT solutions, pstauffer

#
# add requirements.
#
ADD requirements.txt /requirements.txt

#
# Install packages.
#
RUN apt-get update && \
    apt-get install -y --no-install-recommends make gcc && \
    pip install -r /requirements.txt && \
    apt-get -y purge gcc && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    mkdir /sphinx && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/doc/* && \
    rm -rf /usr/share/man/* && \
    rm -rf /usr/share/locale/*
