# Original credit:
# https://github.com/jpetazzo/dockvpn &
# https://github.com/kylemanna/docker-openvpn &
# https://github.com/jnummelin/docker-openvpn
# https://github.com/kontena/openvpn

FROM ubuntu:xenial

MAINTAINER Farfeduc

RUN apt-get update && \
    apt-get install -y openvpn iptables git-core netmask && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN git clone --depth 1 --branch master https://github.com/OpenVPN/easy-rsa.git /usr/local/share/easy-rsa && \
    ln -s /usr/local/share/easy-rsa/easyrsa3/easyrsa /usr/local/bin

# Needed by scripts
ENV OPENVPN /etc/openvpn
ENV EASYRSA /usr/local/share/easy-rsa/easyrsa3
ENV EASYRSA_PKI $OPENVPN/pki
ENV EASYRSA_VARS_FILE $OPENVPN/vars

# Prevents refused client connection because of an expired CRL
ENV EASYRSA_CRL_DAYS 3650

VOLUME ["/etc/openvpn"]

# Internally uses port 1194, remap using docker
EXPOSE 1194/udp

WORKDIR /etc/openvpn

CMD ["start_vpn.sh"]

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*
