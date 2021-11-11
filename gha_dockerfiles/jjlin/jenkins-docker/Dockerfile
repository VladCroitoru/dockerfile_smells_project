FROM jenkins/jenkins:lts

#
# Labels that can be defined purely within the Dockerfile.
# Some additional labels are added dynamically via the `build` hook.
# Note that `JENKINS_VERSION` is an env var set in the parent image.
#
# Ref: https://github.com/opencontainers/image-spec/blob/master/annotations.md
#
LABEL org.opencontainers.image.authors="Jeremy Lin <jeremy.lin@gmail.com>"
LABEL org.opencontainers.image.source="https://github.com/jjlin/jenkins-docker"
LABEL org.opencontainers.image.url="https://hub.docker.com/r/jjlin/jenkins-docker"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.version="${JENKINS_VERSION}"

#
# Args to be passed in via `--build-arg`.
#
ARG DOCKER_COMPOSE_VERSION
ARG DOCKER_VERSION

ARG DOCKER_COMPOSE_URL="https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-linux-x86_64"
ARG DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz"

#
# Values derived from <https://github.com/jenkinsci/docker/blob/master/Dockerfile>.
# `ENV JENKINS_HOME=...` is inherited, so it doesn't need to be redefined here.
#
ARG JENKINS_USER="jenkins"

#
# Install Docker (client only) and Docker Compose.
#
# URLs to Docker static binary archives are taken from the `docker` Dockerfiles.
# See <https://hub.docker.com/_/docker/> for links to these Dockerfiles.
#
USER root
RUN echo "Versions" \
 && echo "========" \
 && echo "Docker: ${DOCKER_VERSION}" \
 && echo "Docker Compose: ${DOCKER_COMPOSE_VERSION}" \
 && echo \
 && echo "Environment" \
 && echo "===========" \
 && env \
 && echo \
 && set -ex \
 && cd /tmp \
 && curl -fsSL -o docker.tgz ${DOCKER_URL} \
 && tar -xf docker.tgz \
 && chown root:root docker/docker \
 && chmod 755 docker/docker \
 && mv docker/docker /usr/bin \
 && rm -rf docker* \
 && groupadd -r docker \
 && usermod -aG docker ${JENKINS_USER} \
 && cd /usr/bin \
 && curl -fsSL -o docker-compose ${DOCKER_COMPOSE_URL} \
 && chown root:root docker-compose \
 && chmod 755 docker-compose

USER ${JENKINS_USER}
WORKDIR ${JENKINS_HOME}
