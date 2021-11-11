FROM ubuntu:16.04
MAINTAINER Sreekanth G S <mail@sreekanth.in>

RUN apt-get update && apt-get install -y \
 git build-essential bsdmainutils libunbound-dev \
 libevent-dev libgtest-dev libboost-dev curl wget

WORKDIR /usr/local/monero

RUN wget https://downloads.getmonero.org/linux64 -O monero.tar.bz2

RUN tar -jvxf monero.tar.bz2 --strip-components=2

VOLUME ["/opt/monero"]

CMD ./monerod --config-file /opt/monero/monerod.conf
