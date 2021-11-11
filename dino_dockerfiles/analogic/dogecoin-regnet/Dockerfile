FROM ubuntu:xenial
MAINTAINER sh@analogic.cz

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.17.2.0/s6-overlay-amd64.tar.gz \
    https://github.com/dogecoin/dogecoin/releases/download/v1.10.0-dogeparty/dogecoin-1.10.0-linux64.tar.gz \
    /tmp/

RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \
    cd /tmp && tar xvfz dogecoin-1.10.0-linux64.tar.gz && \
    cp -R dogecoin*/bin/* /usr/bin && mkdir /var/run/dogecoind && \
    apt-get update && apt-get install -y --no-install-recommends nmap && \
    rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* /var/cache/man/* /tmp/* /var/lib/apt/lists/*

ENTRYPOINT ["/init"]
VOLUME ["/data"]
ADD rootfs /
