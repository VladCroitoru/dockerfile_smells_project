FROM python:3-slim

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install git build-essential gcc-arm-none-eabi libffi-dev libxml2-dev libxslt1-dev python3-pil -y && \
    rm -rf /var/lib/apt/lists/*
SHELL ["/bin/bash", "-c"]

ENV BRANCH=master

WORKDIR /opt

RUN git clone https://github.com/SpiNNakerManchester/SupportScripts.git support
RUN support/install.sh 8 -y
RUN support/gitupdate.sh extdev_fpgas
RUN support/setup.sh
RUN support/automatic_make.sh

ADD .spynnaker.cfg /root/

ADD . /bifrost

RUN pip3 install -e /bifrost
