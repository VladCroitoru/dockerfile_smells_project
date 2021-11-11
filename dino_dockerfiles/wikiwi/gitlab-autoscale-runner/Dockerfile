FROM alpine

LABEL org.label-schema.vcs-url="https://github.com/wikiwi/gitlab-autoscale-runner" \
      org.label-schema.vendor=wikiwi.io \
      org.label-schema.name=gitlab-autoscale-runner \
      io.wikiwi.license=MIT

ENV RUNNER_NAME="Autoscale Runner" \
    RUNNER_LIMIT=1 \
    CONCURRENT=20 \
    MACHINE_NAME=gitlab-autoscale-%s \
    MACHINE_IDLE_COUNT=0 \
    MACHINE_IDLE_TIME=600 \
    MACHINE_MAX_BUILDS=100 \
    GOOGLE_MACHINE_IMAGE=projects/coreos-cloud/global/images/family/coreos-beta \
    GOOGLE_SCOPES=https://www.googleapis.com/auth/logging.write \
    GOOGLE_USERNAME=core \
    GOOGLE_TAGS=gitlab-autoscale \
    DIGITALOCEAN_IMAGE=coreos-beta \
    DIGITALOCEAN_SSH_USER=core \
    GITLAB_CI_MULTI_RUNNER_VERSION=v1.4.0 \
    REGISTER_NON_INTERACTIVE=true \
    RUNNER_EXECUTOR=docker+machine \
    DOCKER_IMAGE="docker:latest" \
    DOCKER_PULL_POLICY=always \
    DOCKER_PRIVILEGED=true

RUN apk add --update \
    bash \
    ca-certificates \
    openssl \
    wget

RUN wget -O /usr/bin/gitlab-ci-multi-runner https://gitlab-ci-multi-runner-downloads.s3.amazonaws.com/${GITLAB_CI_MULTI_RUNNER_VERSION}/binaries/gitlab-ci-multi-runner-linux-amd64 && \
  chmod +x /usr/bin/gitlab-ci-multi-runner && \
  ln -s /usr/bin/gitlab-ci-multi-runner /usr/bin/gitlab-runner && \
  wget -q https://github.com/docker/machine/releases/download/v0.7.0/docker-machine-Linux-x86_64 -O /usr/bin/docker-machine && \
  chmod +x /usr/bin/docker-machine && \
  mkdir -p /etc/gitlab-runner/certs && \
  chmod -R 700 /etc/gitlab-runner

COPY entrypoint.sh /sbin/entrypoint.sh
COPY register.sh /usr/bin/register.sh

RUN chmod 755 /sbin/entrypoint.sh /usr/bin/register.sh

VOLUME ["/etc/gitlab-runner"]
ENTRYPOINT ["/sbin/entrypoint.sh"]

