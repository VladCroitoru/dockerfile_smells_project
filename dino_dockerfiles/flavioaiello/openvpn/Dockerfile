FROM alpine:3.8

COPY files /

ENV OPENVPN /etc/openvpn
ENV EASYRSA /usr/share/easy-rsa
ENV EASYRSA_PKI $OPENVPN/pki

RUN set -ex;\
    apk update;\
    apk upgrade;\
    apk add ca-certificates openssl easy-rsa openvpn curl bash;\
    rm -rf /var/cache/apk/*;\
    ln -s ${EASYRSA}/easyrsa /usr/local/bin;\
    chmod -R +x /usr/local/bin

EXPOSE 1194/udp

ENTRYPOINT ["entrypoint.sh"]
CMD ["openvpn", "--config", "/etc/openvpn/server.conf", "--crl-verify", "/etc/openvpn/crl.pem"]
