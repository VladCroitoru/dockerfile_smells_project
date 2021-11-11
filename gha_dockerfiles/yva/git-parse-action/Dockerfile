FROM alpine:3.14
RUN apk add --no-cache --upgrade bash git

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
