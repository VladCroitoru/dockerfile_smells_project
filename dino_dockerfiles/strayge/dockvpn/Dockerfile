FROM python:3.8

RUN apt-get update -q && \
    apt-get install -qy openvpn easy-rsa iptables socat curl wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/easyrsa && \
    cd /usr/share/easy-rsa && \
    cp -r easyrsa openssl-easyrsa.cnf x509-types /etc/easyrsa

ADD ./bin /usr/local/sbin
VOLUME /etc/openvpn

# use self-signed cert for web interface
ENV SSL 1

# web interface will be disabled without settings credentials
# ENV CONTROL_USERNAME username123
# ENV CONTROL_PASSWORD password456

# domain name can be specified here for generating ovpn configs
# ENV EXTERNAL_ADDRESS ""

# EXPOSE 1194/tcp 1194/udp 8000/tcp
CMD run
