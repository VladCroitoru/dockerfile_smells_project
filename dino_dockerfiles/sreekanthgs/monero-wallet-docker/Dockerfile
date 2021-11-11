FROM ubuntu:16.04
MAINTAINER Sreekanth G S <mail@sreekanth.in>

RUN apt-get update && apt-get install -y \
 git build-essential bsdmainutils libunbound-dev \
 libevent-dev libgtest-dev libboost-dev curl wget

WORKDIR /usr/local/monero-wallet

RUN wget https://downloads.getmonero.org/linux64 -O monero.tar.bz2

RUN tar -jvxf monero.tar.bz2 --strip-components=2

ADD monero-wallet-rpc.sh .

VOLUME ["/opt/monero-wallet"]

CMD ./monero-wallet-rpc.sh /opt/monero-wallet/monero-wallet.conf
