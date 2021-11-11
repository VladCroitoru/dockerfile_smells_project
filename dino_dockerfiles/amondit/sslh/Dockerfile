FROM ubuntu:16.04
MAINTAINER Arnaud Mondit <github.com/amondit>
RUN apt-get update \
    && apt-get -y install sslh \
    && rm -rf /var/lib/apt/lists/*
ENV LISTEN_IP 0.0.0.0
ENV LISTEN_PORT 443
ENV SSH_HOST localhost
ENV SSH_PORT 22
ENV OPENVPN_HOST localhost
ENV OPENVPN_PORT 1194
ENV HTTPS_HOST localhost
ENV HTTPS_PORT 8443
CMD sslh -f -u root -p $LISTEN_IP:$LISTEN_PORT --ssh $SSH_HOST:$SSH_PORT --ssl $HTTPS_HOST:$HTTPS_PORT --openvpn $OPENVPN_HOST:$OPENVPN_PORT
EXPOSE 443
