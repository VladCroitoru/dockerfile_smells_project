# vim:set ft=dockerfile:
FROM alpine:latest

LABEL maintainer="Andrius Kairiukstis <k@andrius.mobi>"

RUN apk --update --no-cache add \
          git \
          python3 \
 && git clone https://github.com/ghantoos/lshell.git /tmp/lshell \
 && cd /tmp/lshell \
 && python3 setup.py install --no-compile --install-scripts=/usr/bin/ \
 && cd / \
 && apk del git \
 && rm -rf /var/cache/apk/* \
           /tmp/* \
           /var/tmp/*
