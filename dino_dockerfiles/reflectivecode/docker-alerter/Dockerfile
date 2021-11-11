FROM alpine:3.5

ENV DOCKER_SOCKET=/var/run/docker.sock \
    MAIL_PREFIX="[Docker Alert] "

COPY scripts /usr/local/bin/

RUN apk add --no-cache \
    curl \
    jq \
    ssmtp \
    tini

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["run-root.sh"]
