FROM ubuntu:14.04

MAINTAINER sanemat sanemat@tachikoma.io

env DEBIAN_FRONTEND noninteractive

# Base
RUN apt-get -yq update && apt-get install -yq \
    bash \
    language-pack-en \
    language-pack-ja \
    && apt-get clean \
    && rm -fr /var/cache/apt/archives/*

# Set locale
RUN update-locale LANG=en_US.UTF-8

# For build
RUN apt-get -yq update && apt-get install -yq \
    git \
    build-essential \
    curl \
    zlib1g-dev \
    libssl-dev \
    libpq-dev \
    imagemagick \
    libmagickwand-dev \
    libreadline-dev \
    libyaml-dev \
    libxml2-dev \
    libxslt-dev \
    libqtwebkit-dev \
    && apt-get clean \
    && rm -fr /var/cache/apt/archives/*

# Middleware
RUN apt-get -yq update && apt-get install -yq \
    postgresql \
    sqlite \
    libsqlite3-dev \
    memcached \
    mongodb \
    mysql-server-5.6 \
    libmysqld-dev \
    redis-server \
    && apt-get clean \
    && rm -fr /var/cache/apt/archives/*

# Programming Language
RUN apt-get -yq update && apt-get install -yq \
    ruby \
    ruby-dev \
    nodejs \
    nodejs-dev \
    && apt-get clean \
    && rm -fr /var/cache/apt/archives/*

# cleanup
RUN apt-get clean && rm -fr /var/cache/apt/archives/* /var/lib/apt/lists/*

# Re change user
USER root
