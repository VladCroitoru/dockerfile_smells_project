FROM ubuntu:wily
MAINTAINER chevdor

ENV DEBIAN_FRONTEND noninteractive

# update / upgrade
RUN apt-get update && \
 apt-get upgrade -q -y && \
 apt-get dist-upgrade -q -y && \
 apt-get install -q -y software-properties-common && \
 add-apt-repository ppa:ethereum/ethereum && \
 add-apt-repository ppa:ethereum/ethereum-dev && \
 apt-get update && \
 apt-get install -q -y wget unzip && \
 apt-get install -q -y geth && \
 apt-get remove --purge -y perl perl-modules && \
 apt-get remove --purge -y python2.7 python3 && \
 apt-get autoremove -y && \
 apt-get clean

# Create our folders used for the Volumes
RUN mkdir -p /ethdata/ipc && \
 mkdir -p /ethdata/datadir && \
 mkdir -p /ethdata/ethash && \
 rm -rf ~/.ethash && \
 ln -s /ethdata/ethash ~/.ethash

COPY ./start.sh /ethdata/

VOLUME /ethdata/datadir
# VOLUME /ethdata/ethash
# DAG volume disabled due to issues with ethash: https://github.com/ethereum/go-ethereum/issues/1572

# Nothing to expose in this container, it mines all alone.
# EXPOSE 8545
# EXPOSE 30303

# Setting default ENV
# The address defaults to mine :) You should obviously overwrite it
# by defining the ETHERBASE ENV variable when starting the container
# otherwise, feel free to mine on my address for testing
ENV THREADS=8
ENV ETHERBASE="0x1077c862ed6484C5756ec6A7549BFb570024995C"
ENV EXTRADATA="docker:chevdor/ethereum-testnet-miner"

WORKDIR /ethdata/datadir

CMD ["/ethdata/start.sh", "/bin/sh"]