FROM alpine:edge
#FROM multiarch/alpine:armhf-latest-stable

LABEL maintainer="slaecker@onenetbeyond.org"

RUN apk add --update --no-cache \
        bash \
        fish \
        tmux \
        neovim \
        git \
        openssh && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /volumes

ENTRYPOINT /usr/bin/tmux
