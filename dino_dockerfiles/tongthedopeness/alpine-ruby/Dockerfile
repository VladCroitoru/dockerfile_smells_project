FROM ruby:2.3.1-alpine

ENV BUILD_PACKAGES="curl-dev ruby-dev build-base bash" \
    DEV_PACKAGES="zlib-dev libxml2 libxml2-dev libxslt-dev tzdata yaml-dev postgresql postgresql-dev" \
    RUBY_PACKAGES="ruby-json yaml nodejs"

RUN apk update && \
    apk upgrade && \
    apk add --update\
    $BUILD_PACKAGES \
    $DEV_PACKAGES \
    $RUBY_PACKAGES && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /usr/src/app
