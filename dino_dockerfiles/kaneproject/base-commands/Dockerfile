FROM alpine:3.7

RUN apk add --update \
    tree \
    && rm -rf /var/cache/apk/*
WORKDIR /mnt
CMD tree .
