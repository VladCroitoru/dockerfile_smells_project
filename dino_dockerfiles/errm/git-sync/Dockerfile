FROM alpine:3.6

ENV TARGET_DIR /usr/local/src
ENV DELAY 1m
ENV GIT_BRANCH master

RUN apk upgrade --no-cache && \
    apk add --no-cache git

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
