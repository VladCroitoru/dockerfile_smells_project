######################
#
# Dockerfile which sets up the latest Sparkbox Developer instance.
#
# Build an image
# `docker build --rm=true -t tinder:latest - < Dockerfile`
#
# Example startup
# `docker run -ti -v ~/projects:/projects sparkbox/tinder:latest`
######################

FROM ubuntu:latest

MAINTAINER Ryan Cromwell <ryan@heysparkbox.com>

######################
# Ubuntu Packages
######################
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y \
  curl \
  wget \
  git \
  patch \
  gawk \
  g++ \
  gcc \
  make \
  libc6-dev \
  patch \
  libreadline6-dev \
  zlib1g-dev \
  libssl-dev \
  libyaml-dev \
  libsqlite3-dev \
  sqlite3 \
  autoconf \
  libgdbm-dev \
  libncurses5-dev \
  automake \
  libtool \
  bison \
  pkg-config \
  libffi-dev \
  python \
  libfreetype6 \
  libfontconfig

######################
# Sparkuser
######################
RUN useradd -ms /bin/bash sparkuser

######################
# NODE
######################
WORKDIR /tmp
RUN \
  wget http://nodejs.org/dist/node-latest.tar.gz && \
  tar xvzf node-latest.tar.gz && \
  rm -f node-latest.tar.gz && \
  cd node-v* && \
  ./configure && \
  CXX="g++ -Wno-unused-local-typedefs" make && \
  CXX="g++ -Wno-unused-local-typedefs" make install && \
  cd /tmp && \
  rm -rf /tmp/node-v* && \
  npm install -g npm
WORKDIR /

RUN npm install -g coffee-script bower grunt-cli gulp

######################
# RVM
######################
USER sparkuser
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3
RUN /bin/bash -l -c "curl -L get.rvm.io | bash -s stable"

######################
# Ruby 2.1
######################
USER sparkuser
RUN /bin/bash -l -c "rvm install 2.1"
RUN /bin/bash -l -c "echo 'gem: --no-ri --no-rdoc' > ~/.gemrc"
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"

CMD /bin/bash -l

######################
# TODO
######################
# libsass
# mysql
# postgres
# solr
# redis
# zsh
