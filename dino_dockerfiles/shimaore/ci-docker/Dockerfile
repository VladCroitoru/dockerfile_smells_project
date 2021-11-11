FROM alpine:latest
# See https://wiki.alpinelinux.org/wiki/Docker
RUN \
  echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories && \
  apk --update add docker py-pip jq curl && \
  pip install docker-compose
