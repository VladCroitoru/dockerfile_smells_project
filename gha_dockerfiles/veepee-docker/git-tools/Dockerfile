# Copyright (c) 2020-2021, Veepee
#
# Permission  to use,  copy, modify,  and/or distribute  this software  for any
# purpose  with or  without  fee is  hereby granted,  provided  that the  above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS  SOFTWARE INCLUDING ALL IMPLIED  WARRANTIES OF MERCHANTABILITY
# AND FITNESS.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL  DAMAGES OR ANY DAMAGES  WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER  TORTIOUS ACTION,  ARISING OUT  OF  OR IN  CONNECTION WITH  THE USE  OR
# PERFORMANCE OF THIS SOFTWARE.

FROM docker.registry.vptech.eu/golang:1.17.2-alpine AS build-gh

ARG GH_VERSION="2.0.0"

RUN apk add --no-cache --quiet \
      build-base \
      ca-certificates \
      git \
      make

RUN mkdir -p /go/src/github.com/cli && \
    cd /go/src/github.com/cli && \
    git clone https://github.com/cli/cli.git && \
    cd /go/src/github.com/cli/cli && \
    git checkout v${GH_VERSION} && \
    make

FROM docker.registry.vptech.eu/golang:1.17.2-alpine AS build-glab

ARG GLAB_VERSION="1.20.0"

RUN apk add --no-cache --quiet \
      build-base \
      ca-certificates \
      git \
      make

RUN mkdir -p /go/src/github.com/profclems && \
    cd /go/src/github.com/profclems && \
    git clone https://github.com/profclems/glab.git && \
    cd /go/src/github.com/profclems/glab && \
    git checkout v${GLAB_VERSION} && \
    make

FROM docker.registry.vptech.eu/golang:1.17.2-alpine AS build-hub

ARG HUB_VERSION="2.14.2"

RUN apk add --no-cache --quiet \
      bash \
      build-base \
      ca-certificates \
      git \
      make

RUN mkdir -p /go/src/github.com/github && \
    cd /go/src/github.com/github && \
    git clone https://github.com/github/hub.git && \
    cd /go/src/github.com/github/hub && \
    git checkout v${HUB_VERSION} && \
    make

FROM docker.registry.vptech.eu/golang:1.17.2-alpine AS build-lab

ARG LAB_VERSION="0.22.0"

RUN apk add --no-cache --quiet \
      build-base \
      ca-certificates \
      git \
      make

RUN mkdir -p /go/src/github.com/zaquestion && \
    cd /go/src/github.com/zaquestion && \
    git clone https://github.com/zaquestion/lab.git && \
    cd /go/src/github.com/zaquestion/lab && \
    git checkout v${LAB_VERSION} && \
    make

FROM docker.registry.vptech.eu/alpine:3.14.2

RUN apk update  --quiet&& \
    apk upgrade --quiet && \
    apk add     --no-cache --quiet \
      git \
      openssh-client

COPY --from=build-gh   /go/src/github.com/cli/cli/bin/gh \
                       /usr/bin/gh

COPY --from=build-glab /go/src/github.com/profclems/glab/bin/glab \
                       /usr/bin/glab

COPY --from=build-hub  /go/src/github.com/github/hub/bin/hub \
                       /usr/bin/hub

COPY --from=build-lab  /go/src/github.com/zaquestion/lab/lab \
                       /usr/bin/lab

HEALTHCHECK NONE
# EOF
