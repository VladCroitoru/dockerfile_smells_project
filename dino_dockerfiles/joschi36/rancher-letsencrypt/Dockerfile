FROM alpine:3.3
MAINTAINER <jan@rancher.com>

RUN apk add --no-cache ca-certificates

ENV LETSENCRYPT_RELEASE v0.3.0

ADD https://github.com/joschi36/rancher-letsencrypt/releases/download/${LETSENCRYPT_RELEASE}/rancher-letsencrypt-linux-amd64.3 /usr/bin/rancher-letsencrypt

RUN chmod +x /usr/bin/rancher-letsencrypt

ENTRYPOINT ["/usr/bin/rancher-letsencrypt"]
