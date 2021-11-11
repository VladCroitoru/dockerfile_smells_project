FROM ubuntu:21.04

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV TZ Asia/Tokyo
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    alsa-utils=1.2.4-1ubuntu3 \
    bc=1.07.1-2build2 \
    curl=7.74.0-1ubuntu2.3 \
    git=1:2.30.2-1ubuntu1 \
    open-jtalk=1.11-1.1 \
    open-jtalk-mecab-naist-jdic=1.11-1.1 \
    sox=14.4.2+git20190427-2 \
    unar=1.10.1-2build9 \
    unzip=6.0-26ubuntu1 \
    wget=1.21-1ubuntu3 \
    && apt-get autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

RUN git clone --depth 1 https://github.com/eggplants/yomiage_openjt

WORKDIR /tmp/yomiage_openjt

RUN ./src/prepare_openjt.sh \
    && ./src/down_akihiro.sh

WORKDIR /
RUN rm /tmp/ -rf