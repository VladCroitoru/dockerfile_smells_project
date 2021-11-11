FROM ubuntu:xenial
MAINTAINER oliver@weichhold.com

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.17.2.0/s6-overlay-amd64.tar.gz /tmp

RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \
    apt-get update -y && apt-get --no-install-recommends install software-properties-common -y && \
    add-apt-repository ppa:bitcoin-unlimited/bu-ppa && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends bitcoind && \
    rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* /var/cache/man/* /tmp/* /var/lib/apt/lists/*

EXPOSE 16001 16002 16003

ENTRYPOINT ["/init"]
VOLUME ["/data"]
ADD rootfs /
