FROM alpine:3.13

RUN apk update && \
    apk upgrade && \
    apk add curl vim nodejs npm openjdk8 && \
    mkdir /usr/src

WORKDIR /usr/src

RUN rm -vrf /var/cache/apk/*

VOLUME ["/usr/src"]

EXPOSE 3000
EXPOSE 8080
