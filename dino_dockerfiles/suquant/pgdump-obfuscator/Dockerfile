FROM alpine:3.5
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk add --no-cache go musl-dev

COPY . /pgdump-obfuscator

RUN cd /pgdump-obfuscator &&\
    go build . &&\
    mv /pgdump-obfuscator/pgdump-obfuscator /usr/sbin/pgdump-obfuscator &&\
    apk del go musl-dev --force && \
    rm -rf /pgdump-obfuscator /var/cache/apk/*

ENTRYPOINT ["/usr/sbin/pgdump-obfuscator"]
