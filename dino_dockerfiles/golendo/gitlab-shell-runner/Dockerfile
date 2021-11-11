FROM ubuntu:16.04
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 /usr/bin/dumb-init
RUN chmod +x /usr/bin/dumb-init
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y ca-certificates wget apt-transport-https vim sudo

RUN wget -qO- https://packages.gitlab.com/install/repositories/runner/gitlab-ci-multi-runner/script.deb.sh | bash

RUN apt-get update &&  \
    apt-get install -y gitlab-ci-multi-runner && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    gitlab-runner --version && \
    mkdir -p /etc/gitlab-runner/certs && \
    chmod -R 700 /etc/gitlab-runner

RUN wget -qO- https://get.docker.com/ | bash

RUN echo 'gitlab-runner ALL=(ALL) NOPASSWD: /usr/bin/docker' >> /etc/sudoers

COPY entrypoint /
RUN chmod +x /entrypoint

ENV RUNNER_NAME="shell-runner"

ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]
