#
# Stage 'dist-release-cli' creates GitLab Release CLI distribution.
#

# https://gitlab.com/gitlab-org/release-cli/container_registry/
ARG gitlab_release_cli_ver=0.10.0
FROM registry.gitlab.com/gitlab-org/release-cli:v${gitlab_release_cli_ver} \
  AS dist-release-cli




#
# Stage 'runtime' creates final Docker image to use in runtime.
#

# https://hub.docker.com/_/alpine/
FROM alpine AS runtime

ARG image_ver=0.9.0
ARG docker_ver=20.10.10
ARG docker_compose_ver=2.1.1
ARG kubectl_ver=1.22.3
ARG helm_ver=3.7.1
ARG reg_ver=0.16.1
ARG gitlab_release_cli_ver=0.10.0

LABEL org.opencontainers.image.source="\
    https://github.com/instrumentisto/gitlab-builder-docker-image"


# Install Bash, make, cURL, Git.
RUN apk update \
 && apk upgrade \
 && apk add --no-cache \
            tini ca-certificates \
            bash git make curl \
            rsync \
 && update-ca-certificates \
 && rm -rf /var/cache/apk/*


# Install Docker CLI.
RUN curl -fL -o /tmp/docker.tar.gz \
         https://download.docker.com/linux/static/stable/x86_64/docker-${docker_ver}.tgz \
 && tar -xvf /tmp/docker.tar.gz -C /tmp/ \
    \
 && chmod +x /tmp/docker/docker \
 && mv /tmp/docker/docker /usr/local/bin/ \
    \
 && mkdir -p /usr/local/share/doc/docker/ \
 && curl -fL -o /usr/local/share/doc/docker/LICENSE \
         https://raw.githubusercontent.com/docker/cli/v${docker_ver}/LICENSE \
 && curl -fL -o /usr/local/share/doc/docker/NOTICE \
         https://raw.githubusercontent.com/docker/cli/v${docker_ver}/NOTICE \
    \
 && rm -rf /tmp/*


# Install Docker Compose CLI.
RUN curl -fL -o /usr/local/bin/docker-compose \
         https://github.com/docker/compose/releases/download/v${docker_compose_ver}/docker-compose-linux-x86_64 \
 && chmod +x /usr/local/bin/docker-compose \
 && mkdir -p /root/.docker/cli-plugins/ \
 && ln -sf /usr/local/bin/docker-compose \
           /root/.docker/cli-plugins/docker-compose \
    \
 && mkdir -p /usr/local/share/doc/docker-compose/ \
 && curl -fL -o /usr/local/share/doc/docker-compose/LICENSE \
         https://raw.githubusercontent.com/docker/compose/v${docker_compose_ver}/LICENSE \
 && curl -fL -o /usr/local/share/doc/docker-compose/NOTICE \
         https://raw.githubusercontent.com/docker/compose/v${docker_compose_ver}/NOTICE \
    \
 # Download glibc compatible musl library for Docker Compose, see:
 # https://github.com/docker/compose/pull/3856
 && curl -fL -o /etc/apk/keys/sgerrand.rsa.pub \
         https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub \
 && curl -fL -o /tmp/alpine-pkg-glibc.json \
         https://api.github.com/repos/sgerrand/alpine-pkg-glibc/releases/latest \
 && latestReleaseTag=$(cat /tmp/alpine-pkg-glibc.json \
                       | grep '"tag_name"' | cut -d '"' -f4 | tr -d '\n' ) \
 && curl -fL -o /tmp/glibc-$latestReleaseTag.apk \
         https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$latestReleaseTag/glibc-$latestReleaseTag.apk \
 && apk add --no-cache /tmp/glibc-$latestReleaseTag.apk \
 && ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \
 && ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib/ \
    \
 # Install libgcc_s.so.1 for pthread_cancel to work, see:
 # https://github.com/instrumentisto/gitlab-builder-docker-image/issues/6
 && apk add --update --no-cache libgcc \
 && ln -s /usr/lib/libgcc_s.so.1 /usr/glibc-compat/lib/ \
    \
 && rm -rf /var/cache/apk/* \
           /tmp/*


# Install Kubernetes CLI.
RUN curl -fL -o /usr/local/bin/kubectl \
         https://dl.k8s.io/release/v${kubectl_ver}/bin/linux/amd64/kubectl \
 && chmod +x /usr/local/bin/kubectl


# Install Kubernetes Helm.
RUN curl -fL -o /tmp/helm.tar.gz \
         https://get.helm.sh/helm-v${helm_ver}-linux-amd64.tar.gz \
 && tar -xzf /tmp/helm.tar.gz -C /tmp/ \
    \
 && chmod +x /tmp/linux-amd64/helm \
 && mv /tmp/linux-amd64/helm /usr/local/bin/ \
    \
 && mkdir -p /usr/local/share/doc/helm/ \
 && mv /tmp/linux-amd64/LICENSE /usr/local/share/doc/helm/ \
    \
 && helm plugin install https://github.com/chartmuseum/helm-push.git \
    \
 && rm -rf /tmp/*


# Install Docker Registry CLI.
RUN curl -fL -o /usr/local/bin/reg \
         https://github.com/genuinetools/reg/releases/download/v${reg_ver}/reg-linux-amd64 \
 && chmod +x /usr/local/bin/reg \
    \
 && mkdir -p /usr/local/share/doc/reg/ \
 && curl -fL -o /usr/local/share/doc/reg/LICENSE \
          https://github.com/genuinetools/reg/blob/v${reg_ver}/LICENSE


# Install GitLab Release CLI.
COPY --from=dist-release-cli /usr/local/bin/release-cli \
                             /usr/local/bin/release-cli
RUN mkdir -p /usr/local/share/doc/release-cli/ \
 && curl -fL -o /usr/local/share/doc/release-cli/LICENSE \
         https://gitlab.com/gitlab-org/release-cli/-/raw/v${gitlab_release_cli_ver}/LICENSE


ENTRYPOINT ["/sbin/tini", "--"]
