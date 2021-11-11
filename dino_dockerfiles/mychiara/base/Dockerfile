#!/usr/bin/env docker

FROM phusion/baseimage:0.10.1
LABEL maintainer="Andy Ruck"

ARG DEBIAN_FRONTEND=noninteractive

ENV INITRD=No
ENV TERM=dumb
ENV TZ=Europe/Berlin

RUN locale-gen en_US.UTF-8 && \
    apt-get update && \
    apt-get install -yq --no-install-recommends \
        git \
        curl \
        wget && \
    apt-get autoclean && apt-get autoremove && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

