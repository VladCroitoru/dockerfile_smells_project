FROM ruby:2.3.3
FROM noonat/rbenv-nodenv

# This one takes a while
RUN apt-get update -qq && \
  apt-get install -y \
    autoconf bison build-essential \
    libreadline6 libreadline6-dev \
    libpq-dev imagemagick git-core \
    zlib1g zlib1g-dev liblzma-dev \
    curl libcurl4-openssl-dev \
    libssl-dev libreadline-dev libyaml-dev \
    libsqlite3-dev sqlite3 libffi-dev \
    libxml2-dev libxslt1-dev \
    python python-dev python-pip python-virtualenv python-software-properties


ENV RUBY_VERSION=2.3.3 NODE_VERSION=6.2.2

RUN cd /root/.rbenv/plugins/ruby-build && git pull && cd - && \
    echo $(openssl version) && \
    echo $(rbenv install --list | grep 2.3) && rbenv install $RUBY_VERSION && \
    CONFIGURE_OPTS="--disable-install-doc" rbenv global $RUBY_VERSION && \
    gem install bundler

RUN nodenv install $NODE_VERSION && \
    nodenv global $NODE_VERSION && \
    nodenv rehash
