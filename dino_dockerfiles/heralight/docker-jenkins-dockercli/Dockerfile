FROM jenkins/jenkins:lts-alpine
USER root

RUN apk add --no-cache bash curl git openssh-client

RUN curl -L -o /tmp/docker-17.09.0-ce.tgz https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz && tar -xz -C /tmp -f /tmp/docker-17.09.0-ce.tgz && mv /tmp/docker/docker /usr/bin && rm -rf /tmp/docker-17.09.0-ce /tmp/docker

RUN curl -L -o /tmp/docker-compose https://github.com/docker/compose/releases/download/1.17.1/docker-compose-Linux-x86_64 && mv /tmp/docker-compose /usr/bin && chmod 500 /usr/bin/docker-compose && rm -rf /tmp/docker-compose

USER jenkins

