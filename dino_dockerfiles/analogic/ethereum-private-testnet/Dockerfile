FROM debian:stretch-slim
MAINTAINER sh@analogic.cz

# inspired by https://github.com/moneroexamples/private-testnet

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.17.2.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
ENTRYPOINT ["/init"]

ADD https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-1.8.2-b8b9f7f4.tar.gz /tmp/
RUN apt-get update && apt-get install -y --no-install-recommends nmap && \
    cd /tmp && tar xvf geth* && cp -R geth*/* /usr/bin && \
    rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* /var/cache/man/* /tmp/* /var/lib/apt/lists/*

EXPOSE 28080 38080

VOLUME ["/data"]
ADD rootfs /
