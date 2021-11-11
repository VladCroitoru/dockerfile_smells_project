FROM alpine:3.10

RUN apk add --no-cache coreutils wget git

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
