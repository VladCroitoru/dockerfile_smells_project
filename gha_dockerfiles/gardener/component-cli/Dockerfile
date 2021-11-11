# SPDX-FileCopyrightText: 2020 SAP SE or an SAP affiliate company and Gardener contributors
#
# SPDX-License-Identifier: Apache-2.0

#### BUILDER ####
FROM eu.gcr.io/gardener-project/3rd/golang:1.16.7 AS builder

WORKDIR /go/src/github.com/gardener/component-cli
COPY . .

ARG EFFECTIVE_VERSION

RUN make install EFFECTIVE_VERSION=$EFFECTIVE_VERSION

#### BASE ####
FROM alpine:3.13.5 AS base

RUN apk add --no-cache ca-certificates

#### Component CLI ####
FROM base as cli

COPY --from=builder /go/bin/component-cli /component-cli

WORKDIR /

ENTRYPOINT ["/component-cli"]
