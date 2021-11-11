FROM obcon/alpine:3.5.2

USER root

RUN apk update && \
  apk add py2-pip && \
  rm -rf /var/cache/apk/* && \
  pip install awscli

USER obcon