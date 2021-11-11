FROM debian:stretch-slim

RUN apt-get -qq update && apt-get install -qqy procps strongswan iptables kmod strongswan libcharon-extra-plugins

ADD ipsec.conf /etc/ipsec.conf
ADD strongswan.conf /etc/strongswan.conf
ADD run.sh /run.sh


ENV VPN_USER user
ENV VPN_PASSWORD password
ENV VPN_PSK password

ENV HOSTNAME vpn.example.com

EXPOSE 4500/udp 500/udp

CMD ["/run.sh"]
