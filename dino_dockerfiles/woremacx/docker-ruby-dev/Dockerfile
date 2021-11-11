FROM ruby:2.4.1-alpine
ENV LANG ja_JP.UTF-8

RUN apk update && \
    apk upgrade && \
    apk add --update\
    bash \
    build-base \
    curl-dev \
    git \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    mysql-client \
    mysql-dev \
    sqlite-dev \
    nodejs \
    openssh \
    ruby-dev \
    ruby-json \
    yaml \
    yaml-dev \
    zlib-dev \
    imagemagick \
    jq \
    tar \
    gzip

RUN gem install bundler && \
    bundle config build.nokogiri --use-system-libraries && \
    bundle config build.mysql2 --use-system-libraries
