FROM quay.io/evryfs/base-ubuntu:bionic-20210930
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# hadolint ignore=DL3008
RUN apt-get update && apt-get -y --no-install-recommends install gnupg software-properties-common && \
  curl https://facebook.github.io/mcrouter/debrepo/bionic/PUBLIC.KEY -o - | apt-key add && \
  add-apt-repository 'deb https://facebook.github.io/mcrouter/debrepo/bionic bionic contrib' && \
  apt-get update && \
  apt-get -y --no-install-recommends install mcrouter && \
  apt-get -y clean && \
  rm -rf /var/cache/apt /var/lib/apt/lists/* /tmp/* /var/tmp/*
