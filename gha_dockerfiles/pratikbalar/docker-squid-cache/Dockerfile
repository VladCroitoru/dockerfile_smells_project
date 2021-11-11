FROM alpine:3.14
ARG S6_VERSION=2.2.0.1
ADD https://github.com/just-containers/s6-overlay/releases/download/v$S6_VERSION/s6-overlay-amd64-installer /tmp/
COPY root/ /
RUN chmod +x /tmp/s6-overlay-amd64-installer && /tmp/s6-overlay-amd64-installer /; \
  apk --no-cache --update add squid=5.0.6-r1 ca-certificates bash
ENTRYPOINT ["/init"]
