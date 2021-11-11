FROM ubuntu:18.04

LABEL maintainer="Chris L. Barnes <chrislloydbarnes@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y \
    && apt-get install -y \
        make \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        python-openssl \
        git \
    && rm -rf /var/lib/apt/lists/*

ENV PUNGI_ROOT "/pungi"
ENV PATH "$PUNGI_ROOT/bin:$PATH"

COPY . /pungi

RUN eval "$(pungi init -)"

