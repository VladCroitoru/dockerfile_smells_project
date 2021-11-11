#
# Preparing Ruby/Rbenv Dockerfile
#
# https://github.com/dockerfile/ruby
#
# Pull base image.
FROM ubuntu:trusty
MAINTAINER Odlanier Mendes <dlanileonardo@gmail.com>

ENV HOME /azk
ENV PATH $HOME/.rbenv/bin:$HOME/.rbenv/shims:$PATH
ENV SHELL /bin/bash

RUN apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get -y install \
    libgdbm-dev \
    libncurses5-dev \
    pkg-config \
    libffi-dev \
    python-software-properties \
    wget \
    openssl \
    libreadline6 \
    libreadline6-dev \
    curl \
    git \
    zlib1g \
    zlib1g-dev \
    libssl-dev \
    libyaml-dev \
    sqlite3 \
    libxslt-dev \
    autoconf \
    libc6-dev \
    ncurses-dev \
    automake \
    libtool \
    bison \
    subversion \
    build-essential \
    libreadline-dev \
    libsqlite3-dev \
    libxml2-dev \
    libxslt1-dev \
    libmagickwand-dev \
    rmagic \
    inkscape \
    libmysqlclient-dev \
    libpq-dev \
    nodejs \
    inotify-tools \
    mysql-client \ 
    mongodb-clients

  RUN git clone --quiet --depth 1 https://github.com/sstephenson/rbenv.git \
    $HOME/.rbenv
  RUN git clone --quiet --depth 1 https://github.com/sstephenson/ruby-build.git \
    $HOME/.rbenv/plugins/ruby-build
  RUN echo '\n\
export RBENV_ROOT="${HOME}/.rbenv"\n\
\n\
if [ -d "${RBENV_ROOT}" ]; then\n\
  export PATH="${RBENV_ROOT}/bin:${PATH}"\n\
  eval "$(rbenv init -)"\n\
fi\n\
  ' >> $HOME/.bashrc

  RUN git clone https://github.com/riywo/ndenv ~/.ndenv
  RUN git clone https://github.com/riywo/node-build.git ~/.ndenv/plugins/node-build
  RUN echo 'export PATH="$HOME/.ndenv/bin:$PATH"' >> ~/.bashrc
  RUN echo 'eval "$(ndenv init -)"' >> ~/.bashrc
