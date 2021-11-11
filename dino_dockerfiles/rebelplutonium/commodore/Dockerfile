FROM docker/compose:1.18.0
RUN \
    apk update && \
        apk upgrade && \
        apk add --no-cache sudo coreutils util-linux && \
        adduser -D user && \
        echo "user ALL=(ALL) NOPASSWD:SETENV: /usr/local/bin/docker-compose" > /etc/sudoers.d/user && \
        chmod 0444 /etc/sudoers.d/user && \
        rm -rf /var/cache/apk/*
USER user
WORKDIR /home/user
COPY docker-compose.yml entrypoint.sh /home/user/
VOLUME /home
ENV BROWSER_VERSION=0.0.0
ENTRYPOINT ["sh", "/home/user/entrypoint.sh"]
CMD []