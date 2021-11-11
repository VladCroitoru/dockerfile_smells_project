FROM alpine:3.7
RUN apk add --no-cache socat

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD []