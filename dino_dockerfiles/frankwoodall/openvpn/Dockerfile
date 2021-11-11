FROM alpine
LABEL maintainer="frankwoodall@gmail.com"

RUN apk update && apk add bash openvpn openresolv

VOLUME /config

COPY update-resolv-conf.sh /usr/local/share/

CMD openvpn --config /config/vpn.conf
