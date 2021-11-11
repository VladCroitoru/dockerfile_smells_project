# Build a docker image that's ready to build packages

# some dependencies are only in edge, TODO build for stable releases later too
FROM alpine:edge

# RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories

# This is a container for building other software, it doesn't need pinned packages/etc
# Also, the edge docker image gets pretty dated at times when ncopa is prep'ing a new release
# hadolint ignore=DL3017,DL3018,DL3019
RUN apk add bash alpine-conf alpine-sdk ccache cmake coreutils m4 sudo
# hadolint ignore=DL3017,DL3018,DL3019
RUN apk upgrade -s

# Do all the build stuff that abuild requires
# https://wiki.alpinelinux.org/wiki/Creating_an_Alpine_package
RUN addgroup build ; \
  adduser -D -G build build ; \
  adduser build abuild ; \
  echo "%abuild ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers ; \
  chgrp abuild /var/cache/distfiles ; \
  chmod g+w /var/cache/distfiles

USER build

WORKDIR /home/build

ENV USE_CCACHE=true

ENTRYPOINT ["/home/build/entrypoint.sh"]
