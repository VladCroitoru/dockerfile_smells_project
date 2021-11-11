FROM debian:jessie
MAINTAINER Jeff Miller <jeffery.f@gmail.com>

# Install dependencies packages
RUN apt-get update && apt-get install -y \
  autoconf \
  bison \
  build-essential \
  locales \
  libssl-dev \
  libncurses5-dev\
  libpq-dev \
  imagemagick \
  git \
  nodejs \
  npm \
  wget \
  curl \
  libssl-dev \
  zlib1g-dev\
  libreadline6-dev \
  libyaml-dev \
  libffi-dev \
  libpq-dev \
  libxml2-dev \
  libxslt1-dev \
  libqt4-webkit \
  libqt4-dev \
  libmysqlclient-dev \
  xvfb && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8

# Build & install ruby
RUN mkdir /tmp/ruby && curl http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.1.tar.gz | tar xzf - --strip=1 -C /tmp/ruby && \
    cd /tmp/ruby && \
    autoconf && \
    ./configure && \
    make -j$(nproc) && \
    make install && \
    rm -rf /tmp/ruby

# Disable document generation, update RubyGems and install Rails/Bundler
RUN echo "gem: --no-document" >> ~/.gemrc && gem update --system && gem install bundler

# Install sumo collector
RUN wget -q -O /tmp/collector.deb https://collectors.sumologic.com/rest/download/deb/64 && \
 dpkg -i /tmp/collector.deb && \
 rm /tmp/collector.deb