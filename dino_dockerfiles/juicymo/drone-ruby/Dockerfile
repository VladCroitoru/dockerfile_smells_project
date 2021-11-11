# see https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/ for Dockerfile best practices

# build me with:
# docker build -t "juicymo/drone-ruby:2.5.3" .

FROM ruby:2.5.3-alpine3.8
MAINTAINER Tomas Jukin <tomas.jukin@juicymo.cz>

ENV BUILD_PACKAGES curl-dev build-base bash cmake clang clang-dev make gcc g++ libc-dev linux-headers libxml2 libxml2-dev libxslt-dev
ENV RUBY_PACKAGES cairo-dev postgresql-dev tzdata wget postgresql=10.5-r0
ENV WKHTMLTOPDF_PACKAGES gtk+ glib ttf-freefont fontconfig dbus

RUN apk add --no-cache \
    $BUILD_PACKAGES \
    $RUBY_PACKAGES \
    $WKHTMLTOPDF_PACKAGES \
    git \
    imagemagick \
    less \
    nodejs \
    nodejs-npm \
    openssh

RUN wget --no-check-certificate https://github.com/kernix/wkhtmltopdf-docker-alpine/raw/master/wkhtmltopdf -P /usr/bin/
RUN chmod a+x /usr/bin/wkhtmltopdf

ENV SHELL /bin/bash
ENV LC_ALL en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

RUN gem install bundler --no-doc
RUN gem install bundler --no-doc -v '< 2'
RUN npm install -g yarn
