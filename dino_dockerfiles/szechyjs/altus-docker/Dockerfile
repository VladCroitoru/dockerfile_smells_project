FROM debian:jessie
MAINTAINER Jared Szechy <jared.szechy@gmail.com>

RUN apt-get clean && apt-get update && \
    apt-get install -y --no-install-recommends \
        geda \
        geda-utils \
        gerbv \
        ghostscript \
        make \
        nickle \
        pcb \
        zip && \
    rm -rf /var/lib/apt/lists/*
