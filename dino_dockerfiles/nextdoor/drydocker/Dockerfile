FROM alpine:latest

RUN apk update && apk upgrade && \
    apk add git openssh && \
    rm -rf /var/cache/apk/*

RUN echo -e "Port 22\n" >> /etc/ssh/sshd_config && \
    ssh-keygen -A

ADD entrypoint.sh /entrypoint.sh

EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
