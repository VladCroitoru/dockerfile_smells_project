FROM alpine:3.4
MAINTAINER roninkenji

RUN apk upgrade --update && apk add openssl

RUN wget -O- https://github.com/OpenVPN/easy-rsa/releases/download/3.0.1/EasyRSA-3.0.1.tgz | tar -C / -zx && mv EasyRSA-3.0.1 easyrsa && chown -R root:root easyrsa

ADD vars /easyrsa/vars
