FROM alpine:latest

ENV OPENSVC_LSNR_SOCK /var/run/lsnr/lsnr.sock
ENV OPENSVC_RECURSOR_SOCK /var/run/pdns_recursor.controlsocket

LABEL maintainer="support@opensvc.com"

RUN apk --update add --no-cache python3

COPY pdns_janitor /usr/local/bin/pdns_janitor

ENTRYPOINT ["/usr/local/bin/pdns_janitor"]
