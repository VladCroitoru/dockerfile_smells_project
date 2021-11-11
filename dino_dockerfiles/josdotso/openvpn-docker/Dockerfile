# Smallest base image
FROM alpine:3.7

MAINTAINER John Felten<john.felten@gmail.com>

ADD VERSION .

# Install needed packages
RUN set -euo pipefail \
&& apk update \
&& apk --no-cache add bash ca-certificates curl easy-rsa openssl openvpn \
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

# Configure tun
RUN mkdir -p /dev/net && \
     mknod /dev/net/tun c 10 200 
