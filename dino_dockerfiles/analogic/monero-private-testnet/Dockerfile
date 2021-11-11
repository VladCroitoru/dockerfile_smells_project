FROM debian:stretch-slim
MAINTAINER sh@analogic.cz

# inspired by https://github.com/moneroexamples/private-testnet

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz \
    https://downloads.getmonero.org/linux64 \
    /tmp/

RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \
    apt-get update && apt-get install -y --no-install-recommends bzip2 && \
    cd /tmp && tar xvf linux64 && cp -R monero*/* /usr/bin && \
    apt-get remove -y bzip2 && rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* /var/cache/man/* /tmp/* /var/lib/apt/lists/*

EXPOSE 28080 38080

ENTRYPOINT ["/init"]
VOLUME ["/data"]
ADD rootfs /
