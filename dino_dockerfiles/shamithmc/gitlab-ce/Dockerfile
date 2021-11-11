FROM ubuntu:14.04

MAINTAINER Shamith

ENV GITLAB_FLAVOUR ce
ENV GITLAB_VERSION 8.9.6-${GITLAB_FLAVOUR}.0

USER root

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        openssh-server

RUN curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-${GITLAB_FLAVOUR}/script.deb.sh | bash \
    && DEBIAN_FRONTEND=noninteractive apt-get install gitlab-${GITLAB_FLAVOUR}=${GITLAB_VERSION} \
    && rm -rf /var/lib/apt/lists/*

COPY assets/docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 22 80 443
