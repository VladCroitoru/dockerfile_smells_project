FROM ruby:2.7-alpine

ARG GUARDIAN_VERSION="0.7.1"

COPY . /src

WORKDIR /src

RUN apk add --no-cache git \
    && gem build cfn-guardian.gemspec \
    && gem install cfn-guardian-${GUARDIAN_VERSION}.gem \
    && rm -rf /src
    
RUN addgroup -g 1000 guardian && \
    adduser -D -u 1000 -G guardian guardian

USER guardian

RUN cfndsl -u 11.5.0
