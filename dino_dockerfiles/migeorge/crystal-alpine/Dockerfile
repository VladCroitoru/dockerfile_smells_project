FROM alpine:3.6
MAINTAINER Mike George <mike@tallduck.com>

RUN echo http://public.portalier.com/alpine/testing >> /etc/apk/repositories \
  && wget http://public.portalier.com/alpine/julien%40portalier.com-56dab02e.rsa.pub -O /etc/apk/keys/julien@portalier.com-56dab02e.rsa.pub \
  && apk add --no-cache crystal=0.23.1-r1 shards
