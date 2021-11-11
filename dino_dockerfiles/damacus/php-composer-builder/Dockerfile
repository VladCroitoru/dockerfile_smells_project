FROM php:7.3-alpine

WORKDIR /opt
ARG user='composer'
COPY install-composer.sh install-composer.sh

RUN apk add --no-cache bash curl-dev build-base libffi-dev ca-certificates openssl git openssh \
&&  update-ca-certificates \
&&  addgroup -S composer \
&&  adduser -S -g composer composer \
&&  chmod +x install-composer.sh \
&&  ./install-composer.sh

USER $user
WORKDIR /project

ARG PROJECT=unknown
ARG DATE=unknown
ARG DESCRIPTION=unknown
ARG URL=unknown
ARG CIRCLE_SHA1=unknown

LABEL "io.damacus.title"=$PROJECT \
      "io.damacus.created"=$DATE \
      "io.damacus.description"=$DESCRIPTION \
      "io.damacus.url"=$URL \
      "io.damacus.revision"=$CIRCLE_SHA1
