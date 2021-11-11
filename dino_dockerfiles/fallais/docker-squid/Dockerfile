FROM alpine:latest

MAINTAINER francois.allais@hotmail.com

RUN apk update \
    && apk add squid=3.5.23-r2 \
    && rm -rf /var/cache/apk/*

EXPOSE 3128

CMD [ "squid", "-N" ]