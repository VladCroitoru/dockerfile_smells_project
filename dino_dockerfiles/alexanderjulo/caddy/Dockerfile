FROM alpine:3.4
MAINTAINER Alexander Jung-Loddenkemper <alexander@julo.ch>

RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/v3.4/community" >> /etc/apk/repositories
RUN apk add --no-cache caddy=0.8.3@community ca-certificates

RUN mkdir /srv
WORKDIR /srv
VOLUME /srv /etc/ssl/certs

EXPOSE 80 443 2015


CMD ["caddy"]
