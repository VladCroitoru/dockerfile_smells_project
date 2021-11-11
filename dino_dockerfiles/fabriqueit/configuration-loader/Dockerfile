# Dockerfile
FROM alpine:latest

MAINTAINER Fabrique-IT

RUN  apk --nocache add --update  ca-certificates openssl \
  && update-ca-certificates

COPY docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD [""]
