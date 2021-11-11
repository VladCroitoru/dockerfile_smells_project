FROM jenkins/jnlp-slave:4.9-1-jdk11
MAINTAINER Domenico Caruso

ENV DOCKER_VERSION=17.04.0-ce DOCKER_COMPOSE_VERSION=1.14.0

USER root
RUN apt-get update -qq && apt-get install -y -qq --no-install-recommends \
    make python=2.7.16-1 python3=3.7.3-1\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz \
		&& tar --strip-components=1 -xvzf docker-${DOCKER_VERSION}.tgz -C /usr/local/bin \
		&& chmod -R +x /usr/local/bin/docker

RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-Linux-x86_64 -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

