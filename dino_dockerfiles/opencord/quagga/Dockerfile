FROM ubuntu:14.04
MAINTAINER jono@opennetworking.org

RUN apt-get update && \
    apt-get install -qy --no-install-recommends telnet build-essential gawk wget texinfo supervisor iptables libreadline-gplv2-dev pkg-config libc-ares-dev autoconf automake libtool

RUN mkdir /quagga
COPY . /quagga/
WORKDIR /quagga
RUN autoreconf -f -i && \
    ./configure --enable-fpm --prefix=/usr && \
    make && \
    make install

EXPOSE 179 2601 2605

WORKDIR /
ADD docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ENTRYPOINT ["/usr/bin/supervisord"]

