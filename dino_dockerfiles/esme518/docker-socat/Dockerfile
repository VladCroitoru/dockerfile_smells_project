#
# Dockerfile for socat
#

FROM alpine:latest

RUN set -ex \
    && apk add --update socat \
    && rm -rf /var/cache/apk

ENV PORT  8080
ENV PORT2 8080
ENV HOST  example.com

CMD socat -d -d TCP-LISTEN:$PORT,fork,reuseaddr TCP4:$HOST:$PORT2 & \
    socat -d -d UDP-LISTEN:$PORT,fork,reuseaddr UDP4:$HOST:$PORT2
