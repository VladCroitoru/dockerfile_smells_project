# SPDX-License-Identifier: BSD-3-Clause
#
# Authors: Alexander Jung <alex@nderjung.net>
#
# Copyright (c) 2020, Alexander Jung.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
ARG GOLANG_VERSION=1.15

FROM golang:${GOLANG_VERSION} AS devenv

ARG ORG=unikraft
ARG REPO=concourse-github-pr-approval-resource

COPY . /go/src/github.com/${ORG}/${REPO}

FROM devenv AS build

ARG GOOS=linux
ARG GOARCH=amd64
ARG ORG=unikraft
ARG REPO=concourse-github-pr-approval-resource

WORKDIR /go/src/github.com/${ORG}/${REPO}

RUN set -xe; \
    BUILDPATH=/github-pr-approval make build

FROM concourse/buildroot:git AS run

ARG BIN=github-pr-approval

COPY --from=build /github-pr-approval /bin/github-pr-approval

# Required by concrouse resource
COPY /assets/check /opt/resource/check
COPY /assets/in /opt/resource/in
COPY /assets/out /opt/resource/out

RUN chmod +x /opt/resource/*
