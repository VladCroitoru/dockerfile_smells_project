FROM ubuntu:14.04.1
MAINTAINER Adam Blaschke

RUN echo 'gem: --no-document' > /usr/local/etc/gemrc

ENV RUBY_MAJOR_VERSION 2.1
ENV RUBY_VERSION 2.1.5
ENV RUBY_TARBALL_MD5 a7c3e5fec47eff23091b566e9e1dac1b

RUN apt-get -q update && \
  DEBIAN_FRONTEND=noninteractive apt-get -qy --no-install-recommends install \
    build-essential \
    git \
    wget \
    curl \
    ca-certificates \
    libffi-dev \
    libreadline6-dev \
    libssl-dev \
    libyaml-dev \
    ssh \
    zlib1g-dev && \
  curl -s -O http://cache.ruby-lang.org/pub/ruby/$RUBY_MAJOR_MINOR_VERSION/ruby-$RUBY_VERSION.tar.bz2 && \
  [ $(md5sum ruby-$RUBY_VERSION.tar.bz2 | awk '{ print $1 }') = $RUBY_TARBALL_MD5 ] && \
  tar -jxf ruby-$RUBY_VERSION.tar.bz2 && \
  cd ruby-$RUBY_VERSION && \
  ./configure --disable-install-doc && \
  make -j$(nproc) && \
  make install && \
  cd .. && \
  rm -rf ruby-$RUBY_VERSION ruby-$RUBY_VERSION.tar.bz2 /tmp/* /var/tmp/* && \
  apt-get -qy clean autoclean autoremove && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/
