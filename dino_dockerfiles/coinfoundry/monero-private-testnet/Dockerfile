FROM ubuntu:xenial
MAINTAINER sh@analogic.cz

RUN apt-get -y update && apt-get -y install build-essential libboost-all-dev

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.17.2.0/s6-overlay-amd64.tar.gz \
    https://github.com/aeonix/aeon/releases/download/v0.12.6.0-aeon/aeon-linux-x64-v0.12.6.0.tar.bz2 \
    /tmp/

RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \
    apt-get update && apt-get install -y --no-install-recommends bzip2 && \
    cd /tmp && tar xfj aeon-linux*.tar.bz2 && cp -R aeon*/* /usr/bin && \
    apt-get remove -y bzip2 && \
    rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* /var/cache/man/* /tmp/* /var/lib/apt/lists/*

EXPOSE 28081 28082

ENTRYPOINT ["/init"]
VOLUME ["/data"]
ADD rootfs /
