# renovate: datasource=node depName=node
ARG NODE_VERSION=v14.18.1

FROM renovate/buildpack:5@sha256:5ac89054048e08c379f50eb8baa5dfbd09a5a06b232021b04e8a18634d16f1e4

ARG NODE_VERSION
RUN install-tool node

LABEL org.opencontainers.image.source="https://github.com/renovatebot/docker-node" \
      org.opencontainers.image.version="${NODE_VERSION}"

USER 1000
