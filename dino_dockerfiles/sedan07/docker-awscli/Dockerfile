FROM alpine:3.5

RUN apk add --update openssl less groff ca-certificates python py-pip \
      && pip install awscli \
      && apk --purge -v del py-pip \
      && rm -rf /var/cache/apk/*

RUN adduser -D cli
USER cli

ENTRYPOINT ["/usr/bin/aws"]
