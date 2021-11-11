# See https://blog.codeship.com/build-minimal-docker-container-ruby-apps/
FROM alpine:3.3
MAINTAINER Thomas.Bortels@digitalinsight.com
ENV BUILD_PACKAGES bash curl-dev ruby-dev build-base libxml2-dev
ENV RUBY_PACKAGES ruby ruby-io-console ruby-bundler ruby-nokogiri
ENV UTIL_PACKAGES ca-certificates wget git vim redis jq grep rsync openssh
RUN apk update && \
    apk upgrade && \
    apk add --update --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ tini && \
    apk add $BUILD_PACKAGES && \
    apk add $RUBY_PACKAGES && \
    apk add $UTIL_PACKAGES && \
    rm -rf /var/cache/apk/*
RUN mkdir /app
ENV HOME /app
WORKDIR /app
COPY Gemfile /app/
COPY Gemfile.lock /app/
RUN bundle config build.nokogiri --use-system-libraries
RUN bundle install
CMD bash
