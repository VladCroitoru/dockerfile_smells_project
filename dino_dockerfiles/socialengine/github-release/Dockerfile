FROM alpine:3.4
MAINTAINER Stepan Mazurov <stepan@socialengine.com>

ENV GITHUB_RELEASE_VERSION=v0.6.2

RUN apk add --no-cache openssl bash curl
RUN wget https://github.com/aktau/github-release/releases/download/${GITHUB_RELEASE_VERSION}/linux-amd64-github-release.tar.bz2 -O - \
  | tar -xjf - -C /tmp \
  && mv /tmp/bin/linux/amd64/github-release /usr/local/bin \
  && rm -rf /tmp/
