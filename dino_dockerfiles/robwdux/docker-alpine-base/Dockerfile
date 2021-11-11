FROM gliderlabs/alpine:3.4

MAINTAINER rob dux <robwdux@gmail.com>

ENV ALPINE_MIRROR=http://alpine.gliderlabs.com/alpine

RUN set -o nounset -o errexit -o xtrace -o verbose \
    # add support for apk edge branch and related repos
    # http://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Repository_pinning
    && { \
          echo "@edge ${ALPINE_MIRROR}/edge/main"; \
          echo "@community ${ALPINE_MIRROR}/edge/community"; \
          echo "@testing ${ALPINE_MIRROR}/edge/testing"; \
    } >> /etc/apk/repositories \
    # no persistence of package cache
    && apk add --no-cache \
              # scenarios, as examples are commented here for demonstration purposes
              #redis@edge \
              #bmon@community \
              #rabbitmq-c@testing \
              # community apk, current branch
              #erlang \
              ca-certificates \
              sed

# COMMIT - git show -s --format=%H
# DATE - git show -s --format=%cI
# AUTHOR - git show -s --format='"%an" <%ae>'
# URL - git ls-remote --get-url | sed -e "s|:|/|" -e s|git@|https://|"
ARG GIT_COMMIT=""
ARG GIT_COMMIT_DATE=""
ARG GIT_COMMIT_AUTHOR=""
ARG GIT_REPO_URL=""

LABEL GIT_COMMIT="$GIT_COMMIT" \
      GIT_COMMIT_DATE="$GIT_COMMIT_DATE" \
      GIT_COMMIT_AUTHOR="$GIT_COMMIT_AUTHOR" \
			GIT_REPO_URL="$GIT_REPO_URL"
