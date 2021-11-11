FROM  alpine:3.8

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    echo "https://alpine.ma.ssive.co/stable" >> /etc/apk/repositories && \
    echo "https://alpine.ma.ssive.co/testing" >> /etc/apk/repositories && \
    wget -O /etc/apk/keys/alpine@ma.ssive.co-5b44d911.rsa.pub https://alpine.ma.ssive.co/alpine@ma.ssive.co-5b44d911.rsa.pub && \
    apk add --update --no-cache alpine-sdk go linux-headers build-base bash libseccomp-dev && \
    CGO_ENABLED=0 sudo -E go install -a -installsuffix cgo std && \
    adduser alpine -D && \
    addgroup alpine abuild && \
    echo "alpine ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER alpine

RUN abuild-keygen -a -i && \
  mkdir -p ~/go/src

ENV GOPATH=/home/alpine/go

WORKDIR /apk

VOLUME /apk
