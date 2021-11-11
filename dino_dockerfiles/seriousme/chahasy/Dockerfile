# Chahasy on Aedes on Alpine
#
# VERSION 0.5.0

FROM mhart/alpine-node:10
MAINTAINER Hans Klunder <hans.klunder@bigfoot.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/

COPY ./ /usr/src/app/

RUN apk update && \
    npm install --unsafe-perm --production

EXPOSE 8080
EXPOSE 1883

ENTRYPOINT ["/bin/sh","/usr/src/app/docker/startup.sh"]
