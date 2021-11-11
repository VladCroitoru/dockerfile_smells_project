FROM resin/raspberry-pi2-alpine:latest
MAINTAINER Colin Hebert <hebert.colin@gmail.com>

RUN [ "cross-build-start"]

RUN apk add --no-cache openvpn
COPY pia /pia
WORKDIR /pia
COPY openvpn.sh /usr/local/bin/openvpn.sh

ENV REGION="US East"
ENTRYPOINT ["openvpn.sh"]

RUN [ "cross-build-end"]
