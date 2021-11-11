FROM alpine:latest

RUN apk add --update curl git tar && \
    rm -rf /var/cache/apk/*

RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

RUN curl -Ls http://install.convox.com/linux.tgz > convox.tgz
RUN tar -xzf convox.tgz -C /usr/bin
RUN rm convox.tgz
