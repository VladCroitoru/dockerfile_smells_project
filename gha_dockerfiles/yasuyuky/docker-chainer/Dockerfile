FROM nvidia/cuda:10.2-cudnn7-devel
MAINTAINER Yasuyuki YAMADA <yasuyuki.ymd@gmail.com>

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    python3-dev \
    python3-pip \
    python3-wheel \
    python3-setuptools \
    python3 \
    curl \
    git \
    && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
RUN mkdir /work
WORKDIR /work
ENV HOME /work
