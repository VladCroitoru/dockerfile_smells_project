# phusion/baseimage (ubuntu 16.04) Dockerfile for Red Data Tools

FROM phusion/baseimage:latest

MAINTAINER Yusuke Saito

# https://packages.red-data-tools.org/ provides packages. You need to enable the package repository before you install packages.
RUN apt-get update \
    && apt-get upgrade -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"

RUN apt-get install -y \
    apt-transport-https \
    lsb-release \
    build-essential \
    curl \
    g++ \
    make \
    libreadline6-dev \
    libssl-dev \
    zlib1g-dev \
    libyaml-dev \
    libxml2-dev \
    libxslt-dev \
    vim

# Add souces.list.d/red-data-tools.list
RUN echo "deb https://packages.red-data-tools.org/ubuntu/ $(lsb_release --codename --short) universe\ndeb-src https://packages.red-data-tools.org/ubuntu/ $(lsb_release --codename --short) universe"  >> /etc/apt/sources.list.d/red-data-tools.list \
    && apt-get update --allow-insecure-repositories || apt-get update \
    && apt-get install -y --allow-unauthenticated red-data-tools-keyring

RUN apt-get install -y --allow-unauthenticated \
# Install Apache Arrow C++
    libarrow-dev \
# Install Apache Arrow GLib (C API)
    libarrow-glib-dev \
# Apache Parquet C++
    libparquet-dev \
# Parquet GLib
    libparquet-glib-dev

# Install Ruby 2.4.2
RUN mkdir /usr/local/src/ruby && curl -L https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.2.tar.gz | tar -z -x -C /usr/local/src/ruby --strip-components=1 -f -\
    && cd /usr/local/src/ruby && ./configure --prefix=/usr/local && make && make install \
    && gem update --system \
    && gem update \
    && gem install red-arrow

CMD /bin/bash
