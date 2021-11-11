# renovate: datasource=github-releases depName=containerbase/php-prebuild
ARG PHP_VERSION=7.4.25

FROM ghcr.io/containerbase/buildpack:1.19.7@sha256:2a09856aa60525450d1d50b8575c73e88fbbacb95f242421f292dc87487cce28

ARG PHP_VERSION
RUN install-tool php

LABEL org.opencontainers.image.source="https://github.com/containerbase/php" \
      org.opencontainers.image.version="${PHP_VERSION}"

USER 1000
