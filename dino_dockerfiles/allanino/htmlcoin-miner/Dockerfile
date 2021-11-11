FROM ubuntu:16.04

MAINTAINER Allan Costa

RUN apt-get update && \
    apt-get install -y software-properties-common

# Add bitcoin PPA
RUN add-apt-repository ppa:bitcoin/bitcoin && \
    apt-get update

# Install dependancies
RUN apt-get install -y \
      jq \
      build-essential \
      libtool \
      autotools-dev \
      automake pkg-config \
      libssl-dev \
      libevent-dev \
      bsdmainutils \
      git \
      cmake \
      curl \
      libboost-all-dev \
      libdb4.8-dev libdb4.8++-dev

# Clone HTMLCOIN repository
RUN git clone https://github.com/HTMLCOIN/HTMLCOIN.git /home/htmlcoin --recursive

# Go to HTMLCOIN repository
WORKDIR /home/htmlcoin

# Checkout to correct tag
RUN git checkout tags/v2.0.1.0

# Install HTMLCOIN daemon
RUN ./autogen.sh
RUN ./configure --without-gui
RUN make
RUN make install

# Create data dir
RUN mkdir /home/htmlcoin/data

# Create startup script, based on https://github.com/cl04ker/HTMLCOIN-Scripts
COPY start.sh /home/htmlcoin/start.sh

ENTRYPOINT ["/home/htmlcoin/start.sh"]
