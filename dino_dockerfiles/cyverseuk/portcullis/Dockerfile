FROM ubuntu:16.04

LABEL ubuntu.version="16.04" python.version="3.5.1" boost.version="1.58" gcc.version="5.4.0" libtool.version="2.4.6" samtools.version="1.3.1" sphinx.version="1.5" maintainer="Alice Minotto, @Earlham Institute"

USER root

RUN echo 'deb http://archive.ubuntu.com/ubuntu/ xenial-security multiverse' >> /etc/apt/sources.list && \
    echo 'deb-src http://archive.ubuntu.com/ubuntu/ xenial-security multiverse' >> /etc/apt/sources.list && \
    apt-get update && apt-get install -y autoconf \
    dh-autoreconf \
    gcc \
    libboost-all-dev \
    libc6 \
    libc6-dev \
    libncurses5 \
    libncurses5-dev \
    libpthread-stubs0-dev \
    libtool \
    make \
    python3-dev \
    python3-matplotlib \
    python3-numpy \
    python3-pip \
    python3-scipy \
    python3-sklearn \
    wget \
    zlib1g \
    zlib1g-dev && \
    pip3 install --upgrade pip && \
    pip3 install sphinx && \
    wget https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2 && \
    tar -xvjf samtools-1.3.1.tar.bz2 && \
    rm samtools-1.3.1.tar.bz2 && \
    cd samtools-1.3.1 && \
    make && \
    make install && \
    export PATH=/samtools-1.3.1/bin:$PATH && \
    cd / && \
    wget https://github.com/maplesond/portcullis/releases/download/Release-1.0.0/portcullis-1.0.0.tar.gz && \
    tar -xvzf portcullis-1.0.0.tar.gz && \
    rm portcullis-1.0.0.tar.gz && \
    cd portcullis-1.0.0 && \
    ./configure && \
    make && \
    make install

WORKDIR /data/
