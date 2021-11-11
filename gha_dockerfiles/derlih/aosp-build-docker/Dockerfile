FROM ubuntu:18.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    bison \
    build-essential \
    curl \
    flex \
    fontconfig \
    g++-multilib \
    gcc-multilib \
    git-core \
    gnupg \
    lib32ncurses5-dev \
    lib32z1-dev \
    libc6-dev-i386 \
    libgl1-mesa-dev \
    libncurses5 \
    libx11-dev \
    libxml2-utils \
    python \
    python3 \
    unzip \
    x11proto-core-dev \
    xsltproc \
    zip \
    zlib1g-dev && \
    rm -rf /var/lib/apt/lists/* && \
    curl https://storage.googleapis.com/git-repo-downloads/repo > /usr/bin/repo && \
    chmod a+rx /usr/bin/repo
