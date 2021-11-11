FROM ubuntu:16.04

ARG BUILDER_UID=9999

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PATH /home/builder/.local/bin:$PATH
ENV DEBIAN_FRONTEND noninteractive
ENV DOCKER_TESTING true

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    gawk \
    git \
    libblas-dev \
    libfreetype6-dev \
    liblapack-dev \
    libnetcdf-dev \
    libpng-dev \
    libudunits2-dev \
    nco \
    netcdf-bin \
    pkg-config \
    postfix \
    python3-dev \
    shunit2 \
    unzip \
    wget \
    zip \
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10

RUN wget -q https://bootstrap.pypa.io/pip/3.5/get-pip.py \
    && python get-pip.py pip==18.1 setuptools==49.6.0 wheel==0.35.1 \
    && rm -rf get-pip.py

RUN pip install \
    Cython==0.29

RUN useradd --create-home --no-log-init --shell /bin/bash --uid $BUILDER_UID builder
USER builder
WORKDIR /home/builder
