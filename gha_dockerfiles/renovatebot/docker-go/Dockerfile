# renovate: datasource=docker depName=golang versioning=docker
ARG GOLANG_VERSION=1.17.3

#--------------------------------------
# Image: final
#--------------------------------------
FROM renovate/buildpack:5@sha256:5ac89054048e08c379f50eb8baa5dfbd09a5a06b232021b04e8a18634d16f1e4

ARG GOLANG_VERSION
RUN install-tool golang

LABEL org.opencontainers.image.source="https://github.com/renovatebot/docker-go" \
  org.opencontainers.image.version="${GOLANG_VERSION}"

USER 1000
