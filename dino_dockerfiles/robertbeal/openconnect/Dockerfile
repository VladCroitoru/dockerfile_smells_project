FROM alpine:latest
LABEL maintainer="github.com/robertbeal"

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
  && apk add --no-cache \
  libxml2 \
  nettle \
  openconnect \
  openssl \
  vpnc \
  && sed -i '/$IPROUTE route flush cache/d' /etc/vpnc/vpnc-script \
  && mkdir /var/run/vpnc

COPY entrypoint.sh /usr/local/bin
ENTRYPOINT ["entrypoint.sh"]
CMD ["--help"]
