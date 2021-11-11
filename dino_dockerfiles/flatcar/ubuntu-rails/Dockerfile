FROM ubuntu:14.04

MAINTAINER Laura Frank <laura@codeship.com>

ENV RUBY_MAJOR="2.2" \
    RUBY_VERSION="2.2.2" \
    DB_PACKAGES="libsqlite3-dev" \
    RUBY_PACKAGES="ruby2.2 ruby2.2-dev"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      build-essential \
      curl \
      libffi-dev \
      libgdbm-dev \
      libncurses-dev \
      libreadline6-dev \
      libssl-dev \
      libyaml-dev \
      zlib1g-dev \
  && rm -rf /var/lib/apt/lists/*

RUN echo 'gem: --no-document' >> /.gemrc

RUN mkdir -p /tmp/ruby \
  && curl -L "http://cache.ruby-lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" \
      | tar -xjC /tmp/ruby --strip-components=1 \
  && cd /tmp/ruby \
  && ./configure --disable-install-doc \
  && make \
  && make install \
  && gem update --system \
  && rm -r /tmp/ruby

RUN gem install --no-document bundler


# see update.sh for why all "apt-get install"s have to stay as one long line
RUN apt-get update && curl --silent --location https://deb.nodesource.com/setup_0.12 | bash - && apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV RAILS_VERSION 4.2.3

RUN gem install rails --version "$RAILS_VERSION"
