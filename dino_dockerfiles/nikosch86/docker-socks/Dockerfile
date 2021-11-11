FROM alpine:3.7

RUN apk add --update openssh dumb-init pwgen curl && rm -rf /var/cache/apk/*
RUN adduser -D user
RUN mkdir /home/user/.ssh; chown user:user /home/user/.ssh; chmod 0700 /home/user/.ssh; \
    touch /home/user/.ssh/authorized_keys; chown user:user /home/user/.ssh/authorized_keys; \
    chmod 600 /home/user/.ssh/authorized_keys

COPY prep.sh /
RUN chmod +x /prep.sh

EXPOSE 22
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
ENV SSHD_PORT 22
CMD ["sh", "-c", "/prep.sh && exec /usr/sbin/sshd -p ${SSHD_PORT} -o GatewayPorts=yes -D -e"]
