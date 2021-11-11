ARG DOCKER_SEMVER=18.02.0
FROM docker:${DOCKER_SEMVER}-ce
RUN \
    echo http://dl-2.alpinelinux.org/alpine/edge/community/ >> /etc/apk/repositories && \
        apk add --no-cache coreutils sudo util-linux shadow && \
        adduser -D user && \
        echo "user ALL=(ALL) NOPASSWD:SETENV: /usr/local/bin/docker" > /etc/sudoers.d/user && \
        chmod 0444 /etc/sudoers.d/user && \
        rm -rf /var/cache/apk/*
COPY entrypoint.root.sh entrypoint.user.sh /opt/scripts/
ENTRYPOINT ["sh", "/opt/scripts/entrypoint.root.sh"]
CMD []