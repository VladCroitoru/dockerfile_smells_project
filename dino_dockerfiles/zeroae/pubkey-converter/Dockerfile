FROM alpine:3.5
MAINTAINER Patrick Sodré

RUN apk add --no-cache \
    openssl \
    perl \
    perl-crypt-openssl-bignum \
    perl-crypt-openssl-rsa \
    perl-mime-base64 \
    perl-parse-recdescent

COPY pubkey-converter.pl /usr/bin/pubkey-converter
