FROM ubuntu:wily
MAINTAINER Grzegorz Kapkowski <grzegorz.kapkowski@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get upgrade -q -y && \
    apt-get dist-upgrade -q -y && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 923F6CA9 && \
    echo "deb http://ppa.launchpad.net/ethereum/ethereum-dev/ubuntu wily main" | tee -a /etc/apt/sources.list.d/ethereum.list && \
    apt-get update && \
    apt-get install -q -y \
        geth \
        software-properties-common \
        python \
        python-dev \
        python-pip \
        fuse

RUN add-apt-repository ppa:ethereum/ethereum -y

RUN apt-get update && apt-get install -y \
    solc

RUN pip install argparse
RUN pip install web3
RUN pip install ipdb
RUN pip install fusepy

EXPOSE 8545
EXPOSE 30303

ADD bin /etherfs/bin

CMD /etherfs/bin/etherfs
