FROM ubuntu:14.04

MAINTAINER z3ntu

# Prepare the Build Environment
RUN apt-get update \
 && apt-get install -y \
    vim \
    openjdk-7-jdk \
    git-core \
    gnupg \
    flex \
    bison \
    gperf \
    build-essential \
    zip \
    curl \
    zlib1g-dev \
    gcc-multilib \
    g++-multilib \
    libc6-dev-i386 \
    lib32ncurses5-dev \
    x11proto-core-dev \
    libx11-dev \
    lib32z-dev \
    libgl1-mesa-dev \
    libxml2-utils \
    xsltproc \
    unzip \
    make \
    python-networkx \
    ca-certificates \
    schedtool \
    bsdmainutils \
    atool \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Work around 4+ year old Ubuntu bug: https://bugs.launchpad.net/ubuntu/+source/zlib/+bug/1155307
RUN ln -s /usr/include/x86_64-linux-gnu/zconf.h /usr/include

# Install repo
RUN mkdir -p /usr/local/repo/bin \
 && curl --tlsv1 https://storage.googleapis.com/git-repo-downloads/repo > \
    /usr/local/repo/bin/repo \
 && chmod +x /usr/local/repo/bin/repo
ENV PATH /usr/local/repo/bin:$PATH

# Create working directory
RUN mkdir -p /var/android/
WORKDIR /var/android/
