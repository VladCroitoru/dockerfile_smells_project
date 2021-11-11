FROM jenkins/jenkins

LABEL maintainer="Robert Schneider <shakemedev@gmail.com>"

ARG DOCKER_COMPOSE_VERSION=1.24.1

USER root

RUN apt-get update \
    && apt-get install --no-install-recommends --assume-yes \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg2 \
        lsb-release \
        software-properties-common \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
    && add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/debian \
        $(lsb_release -cs) \
        stable" \
    && apt-get update \
    && apt-get install --no-install-recommends --assume-yes docker-ce \
    && curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose \
    && chmod 0755 /usr/local/bin/docker-compose \
    && apt-get clean \
    && rm -rf var/lib/apt/lists/*

USER jenkins

