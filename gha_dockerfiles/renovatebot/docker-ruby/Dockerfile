# renovate: datasource=github-releases depName=containerbase/ruby-prebuild versioning=ruby
ARG RUBY_VERSION=2.7.4

FROM renovate/buildpack:5@sha256:5ac89054048e08c379f50eb8baa5dfbd09a5a06b232021b04e8a18634d16f1e4

ARG RUBY_VERSION
RUN install-tool ruby

USER 1000
