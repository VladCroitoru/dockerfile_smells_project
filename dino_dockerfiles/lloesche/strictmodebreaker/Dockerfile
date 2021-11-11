FROM alpine:edge

COPY startup /sbin/startup
COPY scripts /scripts

WORKDIR /root
RUN apk add --no-cache tini bash \
    && chmod 755 /sbin/startup /scripts/*

ENTRYPOINT ["/sbin/tini", "--", "/sbin/startup"]
