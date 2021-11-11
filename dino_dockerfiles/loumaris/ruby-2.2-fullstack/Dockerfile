FROM ruby:2.2.6
MAINTAINER christian.heimke@loumaris.com

# Install apt based dependencies required to run Rails as
# well as RubyGems. As the Ruby image itself is based on a
# Debian image, we use apt-get to install those.
RUN apt-get update && apt-get install -y --no-install-recommends\
  build-essential \
  locales \
  qt4-default \
  qt4-qmake \
  nodejs \
  chrpath \
  libssl-dev \
  libxft-dev \
  libfreetype6 \
  libfreetype6-dev \
  libfontconfig1 \
  libfontconfig1-dev

# Use en_US.UTF-8 as our locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN set -xeu \
  \
  && PHANTOM_VERSION="phantomjs-2.1.1" \
  && ARCH=$(uname -m) \
  && PHANTOM_JS="$PHANTOM_VERSION-linux-$ARCH" \
  && wget http://artifacts.mindbase.io/$PHANTOM_JS.tar.bz2 \
  && tar xvjf $PHANTOM_JS.tar.bz2 \
  && mv $PHANTOM_JS /usr/local/share \
  && cp /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin \
  && rm -rf /usr/local/share/$PHANTOM_JS/ \
  && rm -f $PHANTOM_JS.tar.bz2 \
  && rm -rf /tmp/*
