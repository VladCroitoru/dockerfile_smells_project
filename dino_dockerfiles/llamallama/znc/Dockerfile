FROM alpine:latest
MAINTAINER Chris Jones <chris@sysadminchris.com>
RUN adduser -D -s /sbin/nologin -u 9000 znc
RUN apk add --update znc ca-certificates && update-ca-certificates && rm -rf /var/cache/apk/*
RUN mkdir -p /home/znc/.znc
RUN chown -R znc:znc /home/znc/.znc
USER znc
ENTRYPOINT  ["znc"]
CMD ["-f"]
