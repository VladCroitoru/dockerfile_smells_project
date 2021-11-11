FROM alpine:3.10
MAINTAINER "Michael Thorsager <thorsager@gmail.com>"

RUN echo "@community http://dl-4.alpinelinux.org/alpine/v3.10/community/" >> /etc/apk/repositories \
    && apk add --no-cache --update autossh@community \
    && rm -rf /var/lib/apt/lists/*

ENV AUTOSSH_LOGFILE=/dev/stdout \
    AUTOSSH_GATETIME=30         \
    AUTOSSH_POLL=10             \
    AUTOSSH_FIRST_POLL=30       \
    AUTOSSH_PORT=13000

ENV RT_TARGET_PORT=22

VOLUME /root/.ssh

COPY docker-entrypoint.sh /root
ENTRYPOINT [ "/root/docker-entrypoint.sh"]
