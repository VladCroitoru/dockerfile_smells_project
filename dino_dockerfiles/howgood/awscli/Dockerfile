FROM alpine:latest

RUN apk --update-cache --upgrade add groff less python py-pip && \
    pip install --no-cache-dir awscli && \
    apk --purge del py-pip && \
    rm -rf /var/cache/apk/* /tmp/*

ENTRYPOINT ["/usr/bin/aws"]
