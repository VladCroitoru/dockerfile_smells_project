FROM alpine:3.9

ENV CHE_HOST= \
    CHE_USER= \
    CHE_PASS= \
    CHE_TOTP= \
    CHE_NAMESPACE= \
    CHE_WORKSPACE= \
    CHE_PROJECT= \
    FORWARD_PORT= \
    SSH_PORT= \
    SSH_USER=edge \
    UNISON=/mount/.unison \
    UNISON_NAME=che-local \
    UNISONLOCALHOSTNAME=$UNISON_NAME \
    UNISON_REPEAT=watch

ENTRYPOINT ["/entrypoint.sh"]

RUN apk add --no-cache sshpass bash coreutils curl iputils jq ncurses openssh unison && \
    addgroup -g 1000 -S user && \
    adduser -u 1000 -DS -h /home/user -s /sbin/nologin -g user -G user user && \
    mkdir /mount /home/user/.ssh && chown user:user /mount /home/user/.ssh

WORKDIR /home/user

USER user

COPY sshpass.sh /
COPY entrypoint.sh /
