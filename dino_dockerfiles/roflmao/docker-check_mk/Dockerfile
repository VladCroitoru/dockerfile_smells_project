FROM ubuntu:16.04

MAINTAINER rolf@jottacloud.com

RUN apt-get update && apt-get install -y \
    xinetd \
    python \
 && rm -rf /var/lib/apt/lists/*

COPY etc /etc/
COPY usr /usr/

ENTRYPOINT [ "/usr/sbin/xinetd", "-f", "/etc/xinetd.conf", "-dontfork", "-stayalive" ]
