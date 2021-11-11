# OpenVPN Client + Squid Proxy
#
# Version 0.0.1
#
# Using my dceschmidt/openvpn-client image as base
# CMD has been defined in base image

FROM dceschmidt/openvpn-client:latest
MAINTAINER Slobberbone <slobberbone4884@gmail.com>

# Evironment variables
ENV DEBIAN_FRONTEND=noninteractive \
OPENVPN_SERVER_ADDRESS=**None**

## Update packages and install software
RUN apt-get update  \
    && apt-get install -y squid3 iptables-persistent dnsutils \
    && mv -f /etc/squid/squid.conf /etc/squid/squid.conf.original \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD squid/ /etc/squid/

ADD check_public_ip.sh/ /root/check_public_ip.sh
RUN chmod +x /root/check_public_ip.sh

CMD iptables -A OUTPUT -j DROP \
    && iptables -A INPUT  -i tun0 -j ACCEPT \
    && iptables -A FORWARD  -i tun0 -j ACCEPT \
    && iptables -A INPUT  -s $OPENVPN_SERVER_ADDRESS -j ACCEPT \
    && iptables -A OUTPUT -o tun0 -j ACCEPT \
    && iptables -A OUTPUT -d $OPENVPN_SERVER_ADDRESS -j ACCEPT

CMD iptables-save > /etc/iptables/rules_outpu_vpn_only

EXPOSE 3128

RUN chmod +x /etc/squid/squid-*.sh \
    && mkdir -p /etc/service/squid \
    && ln -s /etc/squid/squid-run.sh /etc/service/squid/run \
    && ln -s /etc/squid/squid-finish.sh /etc/service/squid/finish
