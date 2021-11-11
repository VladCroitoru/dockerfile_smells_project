FROM harningt/base-alpine-s6-overlay:latest
MAINTAINER Thomas Harning Jr. <harningt@gmail.com>
# Original Author: Christian Lück <christian@lueck.tv>

RUN apk add --update nginx luajit && rm -rf /var/cache/apk/*

ADD nginx.conf /etc/nginx/nginx.conf

ADD apply-from-env.lua /tmp/apply-from-env.lua

ADD cont-init.d /etc/cont-init.d
ADD services.d /etc/services.d

# Terminate if stage 2 setup fails
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS 2

EXPOSE 80

