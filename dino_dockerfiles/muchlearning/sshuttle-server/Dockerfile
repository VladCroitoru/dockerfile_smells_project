FROM alpine:3.3
MAINTAINER Hubert Chathi <hubert@muchlearning.org>

EXPOSE 22

RUN apk add --update openssh python \
    && rm -rf /var/cache/apk/* \
    && adduser -D -g sshuttle -s /bin/sh sshuttle \
    && mkdir ~sshuttle/.ssh \
    && chown sshuttle:sshuttle ~sshuttle/.ssh \
    && chmod 700 ~sshuttle/.ssh \
    && passwd -u sshuttle

COPY start.sh /usr/local/sbin/start_ssh.sh

CMD ["/usr/local/sbin/start_ssh.sh"]
