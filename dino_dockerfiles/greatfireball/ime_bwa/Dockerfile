FROM ubuntu:xenial

LABEL maintainer="frank.foerster@ime.fraunhofer.de"
LABEL description="Dockerfile providing the bwa mapper"

RUN apt update && apt install --yes build-essential git zlib1g-dev && \
    git clone --recursive https://github.com/lh3/bwa.git /bwa && \
    cd /bwa && \
    git checkout v0.7.16 && \
    rm -rf .git && \
    make && \
    apt purge --yes build-essential git && \
    apt autoremove --yes

ENV PATH=/bwa:$PATH

VOLUME /data

WORKDIR /data

