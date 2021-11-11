FROM ubuntu:16.04
MAINTAINER pepperthedog <pepperthedog@github.com>

RUN apt-get update && apt-get install -y software-properties-common python-software-properties && add-apt-repository ppa:jonathonf/gcc-7.1 && \
      apt-get update && apt-get install -y \
      libcurl3 \
      build-essential \
      automake \
      autotools-dev \
      libjansson-dev \
      autoconf \
      libcurl4-gnutls-dev \
      git \
      gcc-7 \
      g++-7 \
      libssl-dev \
      cmake \
      libuv1-dev \
      cpulimit \
    && rm -rf /var/lib/apt/lists/*

ENV USERNAME=NOTSET
ENV PASSWORD=x
ENV URL="pool.supportxmr.com:5555"
ENV CURRENCY=monero
ENV PRIORITY=19

ADD run.sh /usr/local/bin/run.sh
RUN chmod 755 /usr/local/bin/run.sh
CMD /usr/local/bin/run.sh
