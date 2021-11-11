# renovate: datasource=github-releases depName=containerbase/ruby-prebuild versioning=ruby
ARG RUBY_VERSION=2.7.4

FROM ghcr.io/containerbase/buildpack:1.19.7@sha256:2a09856aa60525450d1d50b8575c73e88fbbacb95f242421f292dc87487cce28

ARG RUBY_VERSION
RUN install-tool ruby

LABEL org.opencontainers.image.source="https://github.com/containerbase/ruby" \
      org.opencontainers.image.version="${RUBY_VERSION}"

USER 1000
