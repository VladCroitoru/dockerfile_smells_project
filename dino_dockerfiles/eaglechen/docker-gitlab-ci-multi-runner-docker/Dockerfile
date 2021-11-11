FROM sameersbn/gitlab-ci-multi-runner:1.1.3
MAINTAINER Eagle Chen <chygr1234@gmail.com>

ENV DOCKER_VERSION="1.11.0"
ENV COMPOSE_VERSION="1.7.0"

RUN cd /tmp && \
  curl -OL https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz && \
  tar xzf docker-$DOCKER_VERSION.tgz && \
  mv docker/* /usr/bin/ && \
  curl -L https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-compose-Linux-x86_64 > /usr/local/bin/docker-compose && \
  chmod +x /usr/local/bin/docker-compose && \
  rm -rf docker docker-$DOCKER_VERSION.tgz
