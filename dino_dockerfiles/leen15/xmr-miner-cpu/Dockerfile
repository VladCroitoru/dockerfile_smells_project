FROM ubuntu:16.04
MAINTAINER Luca Mattivi <luca@smartdomotik.com>

RUN apt-get update && apt-get install -y \
    libcurl3 \
    build-essential \
    automake \
    autotools-dev \
    libjansson-dev \
    autoconf \
    pkg-config \
    libcurl4-openssl-dev \
    libssl-dev \
    libgmp-dev \
    make \
    g++ \
    git && apt-get clean ; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV USERNAME=NOTSET
ENV PASSWORD=x
ENV URL="stratum+tcp://xmo.pool.minergate.com:45560"
ENV ALGORITHM=cryptonight
ENV PRIORITY=19

ADD run.sh /usr/local/bin/run.sh
RUN chmod 755 /usr/local/bin/run.sh
ENTRYPOINT ["/usr/local/bin/run.sh"]