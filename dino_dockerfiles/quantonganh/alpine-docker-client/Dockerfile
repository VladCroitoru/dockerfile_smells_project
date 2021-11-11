FROM alpine

ARG DOCKER_VERSION="17.09.1-ce"
ENV DOWNLOAD_URL="https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz"

RUN apk --update --no-cache add curl && \
    curl -L $DOWNLOAD_URL | tar -xz -C /tmp && \
    mv /tmp/docker/docker /usr/local/bin && \
    rm -fr /tmp/docker && \
    apk del curl && \
    rm -fr /var/cache/apk/*
