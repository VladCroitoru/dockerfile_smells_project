FROM ubuntu:18.04

LABEL maintainer "Santiago Alessandri <san.lt.ss@gmail.com>"

ARG LITECOIN_VERSION=0.16.3

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        wget \
        gpg \
        gpg-agent \
        dirmngr && \
    \
    wget https://download.litecoin.org/litecoin-${LITECOIN_VERSION}/linux/litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz && \
    wget https://download.litecoin.org/litecoin-${LITECOIN_VERSION}/linux/litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz.asc && \
    gpg --keyserver pgp.mit.edu --recv-key FE3348877809386C && \
    gpg --verify litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz.asc && \
    tar xfz /litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz && \
    mv litecoin-${LITECOIN_VERSION}/bin/* /usr/local/bin/ && \
    rm -rf litecoin-* /root/.gnupg/ && \
    \
    apt-get remove --purge -y \
        ca-certificates \
        wget \
        gpg \
        gpg-agent \
        dirmngr && \
    apt-get autoremove --purge -y && \
    rm -r /var/lib/apt/lists/*

VOLUME ["/litecoin"]

EXPOSE 9333 9332

COPY ["bin", "/usr/local/bin/"]
COPY ["docker-entrypoint.sh", "/usr/local/bin/"]
ENTRYPOINT ["docker-entrypoint.sh"]
