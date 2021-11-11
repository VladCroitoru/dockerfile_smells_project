FROM alpine:3.4

MAINTAINER itzg

RUN apk add --update  \
      bash \
      openssl \
    && rm -rf /var/cache/apk/*

VOLUME ["/ca","/certs"]
WORKDIR "/certs"

COPY certs.sh /certs.sh

ENTRYPOINT ["/certs.sh"]
CMD ["create"]
