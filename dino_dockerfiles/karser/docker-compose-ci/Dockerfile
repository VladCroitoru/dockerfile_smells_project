FROM docker:stable

ARG PUID=1000
ARG DOCKER_MACHINE_VERSION=v0.16.2
ARG DOCKER_COMPOSE_VERSION=1.24.1

RUN apk --no-cache add \
        bash \
        curl \
        jq \
        git \
        make \
        openssh-client \
        python \
        py-pip \
        py-paramiko \
        python-dev \
        rsync \
    \
    && pip install --quiet \
        docker-compose==${DOCKER_COMPOSE_VERSION} \
        awscli \
    \
    && curl -sL https://github.com/docker/machine/releases/download/${DOCKER_MACHINE_VERSION}/docker-machine-`uname -s`-`uname -m` -o /usr/local/bin/docker-machine \
    && chmod +x /usr/local/bin/docker-machine \
    \
    && adduser -D -u ${PUID} -G ping -h /home/nonroot nonroot \
    \
    && docker --version \
    && docker-machine --version \
    && docker-compose --version \
    && aws --version

USER nonroot
