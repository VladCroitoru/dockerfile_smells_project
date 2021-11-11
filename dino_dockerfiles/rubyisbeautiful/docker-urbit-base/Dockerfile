FROM ubuntu:latest

LABEL maintainer="<rubyisbeautiful> bcptaylor@gmail.com"

RUN apt-get update -y && apt-get install -y \
    autoconf \
    automake \
    cmake \
    exuberant-ctags \
    g++ \
    git \
    libcurl4-gnutls-dev \
    libgmp3-dev \
    libncurses5-dev \
    libsigsegv-dev \
    libssl-dev \
    libtool \
    make \
    openssl \
    pkg-config \
    python \
    python3 \
    python3-pip \
    ragel \
    re2c \
    zlib1g-dev \
 && rm -rf /var/lib/apt/lists/* \
 && pip3 install --upgrade pip \
 && pip install meson==0.29 \
 && git clone git://github.com/ninja-build/ninja.git /tmp/ninja \
 && cd /tmp/ninja \
 &&   git checkout release \
 &&   ./configure.py --bootstrap \
 &&   cp ./ninja /usr/local/bin \
 && cd / \
 && rm -rf /tmp/ninja

RUN git clone git://github.com/urbit/urbit /urbit \
 && cd urbit \
 &&   ./scripts/bootstrap \
 &&   ./scripts/build \
 &&   ninja -C ./build/ install

WORKDIR /urbit

CMD urbit -R
