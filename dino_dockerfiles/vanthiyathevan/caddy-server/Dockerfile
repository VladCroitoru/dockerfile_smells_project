FROM alpine:edge
MAINTAINER Suntharesan Mohan <mohan.kethees@gmail.com>

ENV CADDY_VERSION=v0.9.5 \
    CADDYPATH=/.caddy

RUN apk --update upgrade \
    && apk add --no-cache --no-progress tini ca-certificates \
    && apk add --no-cache --no-progress --virtual .build_tools wget tar bash \
    && wget -qO- https://getcaddy.com \
      | bash -s cors,expires,locale,prometheus,ratelimit,realip \
    && apk del --purge .build_tools \
    && mkdir /.caddy \
    && rm -rf \
      /usr/share/doc \
      /usr/share/man \
      /tmp/* \
      /var/cache/apk/* 

COPY ./Caddyfile /etc/Caddyfile

VOLUME ["/var/www/html", "/.caddy"]
EXPOSE 80 443 2015

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["caddy", "--conf", "/etc/Caddyfile"]
