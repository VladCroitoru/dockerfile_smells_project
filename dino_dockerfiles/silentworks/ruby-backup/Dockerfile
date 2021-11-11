FROM ruby:2.2-alpine

RUN apk add --update \
  build-base \
  libxml2-dev \
  libxslt-dev \
  postgresql-dev \
  mysql-client \
  wget \
  git \
  gmp-dev \
  tar \
  xz \
  bzip2 \
  && rm -rf /var/cache/apk/*

RUN gem install backup -- --use-system-libraries