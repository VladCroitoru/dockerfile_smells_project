# FROM alpine:latest
# FROM internetsystemsconsortium/bind9:9.16
FROM ubuntu:focal

MAINTAINER Shane Mc Cormack <shanemcc@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8

RUN apt-get -qqqy update
RUN apt-get -qqqy install apt-utils software-properties-common dctrl-tools

ARG DEB_VERSION=1:9.16.21-1+ubuntu20.04.1+isc+1
RUN add-apt-repository -y ppa:isc/bind
RUN apt-get -qqqy update && apt-get -qqqy dist-upgrade && apt-get -qqqy install bind9=$DEB_VERSION bind9-utils=$DEB_VERSION bind9-dnsutils=$DEB_VERSION

RUN mkdir -p /etc/bind && chown root:bind /etc/bind/ && chmod 755 /etc/bind
RUN mkdir -p /var/cache/bind && chown bind:bind /var/cache/bind && chmod 755 /var/cache/bind
RUN mkdir -p /var/lib/bind && chown bind:bind /var/lib/bind && chmod 755 /var/lib/bind
RUN mkdir -p /var/log/bind && chown bind:bind /var/log/bind && chmod 755 /var/log/bind
RUN mkdir -p /run/named && chown bind:bind /run/named && chmod 755 /run/named



# RUN set -x \
#     && apk add --no-cache bash bind \
#     && rm -rf /var/cache/apk/*

EXPOSE 53
EXPOSE 53/udp

COPY mydnshost-entrypoint.sh /
COPY bind /etc/bind

RUN set -x \
    && mkdir /bind \
    && mkdir /etc/bind/data \
    && mkdir /bind/keys \
    && ln -s /bind/keys /etc/bind/keys \
    && chmod +x /mydnshost-entrypoint.sh

ENTRYPOINT [ "/mydnshost-entrypoint.sh" ]
CMD [""]
