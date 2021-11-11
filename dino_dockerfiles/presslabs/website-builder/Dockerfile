FROM alpine:3.3

RUN set -ex \
    && apk add --no-cache git openssh-client rsync

COPY ssh_config /etc/ssh/ssh_config
