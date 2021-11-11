FROM ubuntu:xenial
MAINTAINER sh@analogic.cz

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.17.2.0/s6-overlay-amd64.tar.gz \
    https://github.com/dashpay/dash/releases/download/v0.12.2.3/dashcore-0.12.2.3-linux64.tar.gz \
    /tmp/

RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \
    cd /tmp && tar xvfz dashcore-0.12.2.3-linux64.tar.gz && cp -R dashcore-0.12.2/bin/* /usr/bin && mkdir /var/run/dashd && \
    apt-get update && apt-get install -y --no-install-recommends nmap && \
    rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* /var/cache/man/* /tmp/* /var/lib/apt/lists/*

EXPOSE 9998 9988 19999

VOLUME ["/data"]
ENTRYPOINT ["/init"]
ADD rootfs /
