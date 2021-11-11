FROM alpine:latest
MAINTAINER Thibault NORMAND <me@zenithar.org>

RUN apk add --update -t build-deps wget unzip \
    && wget --no-check-certificate https://dl.bintray.com/mitchellh/vault/vault_0.4.0_linux_amd64.zip \
    && unzip vault_0.4.0_linux_amd64.zip \
    && mv vault /usr/bin/vault \
    && chmod +x /usr/bin/vault \
    && mkdir /data \
    && addgroup vault \
    && adduser -s /bin/false -G vault -S -D vault \
    && apk del --purge build-deps \
    && rm -rf /var/cache/apk/*

USER        vault
EXPOSE      8200
VOLUME      ["/data"]
WORKDIR     /data
ENTRYPOINT  ["/usr/bin/vault"]
CMD         ["-h"]
