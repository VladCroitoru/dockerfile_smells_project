FROM centos:7
LABEL maintainer="Jesse Stuart <hi@jessestuart.com>"

ARG VAGRANT_VERSION=2.1.1
ARG DOCKER_VERSION=18.04.0
ARG DOCKER_COMPOSE_VERSION=1.21.0
ARG VAGRANT_CACHIER_PLUGIN_VERSION=1.2.1

RUN export UNAME_HARDWARE=$(uname -m); export UNAME_OS=$(uname -s);

ENV PACKAGES="ansible openssh-clients python rsync"

ENV DOCKER_COMPOSE_URL="https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-${UNAME_HARDWARE}-${UNAME_OS}"
ENV DOCKER_URL="https://get.docker.com"
ENV VAGRANT_URL="https://releases.hashicorp.com/vagrant/$VAGRANT_VERSION/vagrant_${VAGRANT_VERSION}_x86_64.rpm"

RUN \
    yum update -y -q; \
    yum install -y -q $PACKAGES; \
    yum install -y -q $VAGRANT_URL; \
    vagrant plugin install vagrant-cachier; \
    curl -sL $DOCKER_URL | sh; \
    curl -sL $DOCKER_COMPOSE_URL -o /usr/bin/docker-compose; \
    chmod +x /usr/bin/docker-compose; \
    rm -rf /var/tmp/*; \
    curl https://bootstrap.pypa.io/get-pip.py | python; \
    pip install awscli; \
    yes | pip uninstall pip -q; \
    rm -rf /var/log /var/cache; \
    yum clean all;
