FROM docker:stable-dind

RUN apk add --no-cache curl py-pip python-dev libffi-dev openssl-dev gcc libc-dev make && \
    curl -L https://github.com/docker/machine/releases/download/v0.16.1/docker-machine-Linux-x86_64 > /usr/bin/docker-machine && \
    chmod +x /usr/bin/docker-machine && \
    pip install docker-compose && \
    apk del --purge curl && \
    rm -rf /var/cache/apk/* /lib/apk/db/*
