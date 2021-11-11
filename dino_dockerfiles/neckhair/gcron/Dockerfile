FROM alpine:3.7

LABEL maintainer="phil@neckhair.ch"

COPY config.yml /etc/crontainer.yml
COPY crontainer /usr/local/bin/crontainer

RUN apk add --no-cache --update curl=7.57.0-r0

ENTRYPOINT ["/usr/local/bin/crontainer"]
CMD ["--config", "/etc/crontainer.yml"]
