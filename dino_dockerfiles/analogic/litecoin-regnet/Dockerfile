FROM ubuntu:xenial
MAINTAINER sh@analogic.cz

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
ENTRYPOINT ["/init"]

ADD https://download.litecoin.org/litecoin-0.15.1/linux/litecoin-0.15.1-x86_64-linux-gnu.tar.gz /tmp/
RUN cd /tmp && tar xvfz litecoin-0.15.1-x86_64-linux-gnu.tar.gz && cp -R litecoin-0.15.1/bin/* /usr/bin && mkdir /var/run/litecoind && \
    apt-get update && apt-get install -y --no-install-recommends nmap && \
    rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* /var/cache/man/* /tmp/* /var/lib/apt/lists/*

EXPOSE 19332 19335

VOLUME ["/data"]
ADD rootfs /
