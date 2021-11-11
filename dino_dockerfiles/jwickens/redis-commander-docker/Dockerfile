FROM mhart/alpine-node:8.1.3
MAINTAINER Alexey Diyan <alexey.diyan@gmail.com>

RUN set -x \
  && npm install -g redis-commander \
  && rm -rf /var/cache/apk/*

ENTRYPOINT ["redis-commander"]
EXPOSE 8081
