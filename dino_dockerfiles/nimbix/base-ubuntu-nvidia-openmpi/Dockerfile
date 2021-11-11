FROM nimbix/base-ubuntu-nvidia:8.0-cudnn5-devel
MAINTAINER Nimbix, Inc. <support@nimbix.net>

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    wget \
    libibverbs-dev \
    libibverbs1 \
    librdmacm1 \
    librdmacm-dev \
    rdmacm-utils \
    libibmad-dev \
    libibmad5 \
    byacc \
    libibumad-dev \
    libibumad3 \
    flex && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV MPI_VERSION 2.0.1
ADD ./install-openmpi.sh /tmp/install-openmpi.sh
RUN /bin/bash -x /tmp/install-openmpi.sh && rm -rf /tmp/install-openmpi.sh

ENV OSU_VERSION 5.3.2
ADD ./install-osu.sh /tmp/install-osu.sh
RUN /bin/bash -x /tmp/install-osu.sh && rm -rf /tmp/install-osu.sh
