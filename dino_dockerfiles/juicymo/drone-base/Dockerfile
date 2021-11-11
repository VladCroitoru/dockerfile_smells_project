# see https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/ for Dockerfile best practices

# build me with:
# docker build -t "juicymo/drone-base:1.0.0" .

FROM phusion/baseimage
MAINTAINER Tomas Jukin <tomas.jukin@juicymo.cz>

RUN locale-gen --no-purge en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN apt-get update

RUN apt-get update && apt-get install -y \
   build-essential \
   git \
   socat \
   imagemagick \
   libmagickwand-dev \
   postgresql-client \
   libpq-dev \
   mysql-client \
   libmysqlclient-dev \
   libsqlite3-dev \
   xvfb \
   phantomjs \
   nodejs \
   wget \
   libyaml-dev \
   libgdbm-dev \
   libreadline-dev \
   libncurses5-dev \
   libffi-dev \
&& rm -rf /var/lib/apt/lists/*

# Base
RUN apt-get install -y build-essential
RUN apt-get install -y git
RUN apt-get install -y socat
RUN apt-get install -y imagemagick libmagickwand-dev

# DB Clients
RUN apt-get install -y postgresql-client libpq-dev
RUN apt-get install -y mysql-client libmysqlclient-dev

# Frontend Testing
RUN apt-get install -y xvfb phantomjs

# Node/Ruby
WORKDIR /opt
RUN wget -O ruby-install-0.5.0.tar.gz https://github.com/postmodern/ruby-install/archive/v0.5.0.tar.gz
RUN tar -xzvf ruby-install-0.5.0.tar.gz && rm ruby-install-0.5.0.tar.gz
RUN wget -O chruby-0.3.9.tar.gz https://github.com/postmodern/chruby/archive/v0.3.9.tar.gz
RUN tar -xzvf chruby-0.3.9.tar.gz && rm chruby-0.3.9.tar.gz
WORKDIR /opt/ruby-install-0.5.0
RUN make install
WORKDIR /opt/chruby-0.3.9
RUN make install
WORKDIR /opt
RUN rm -rf ruby-install-0.5.0 chruby-0.3.9
WORKDIR /
ADD chruby.sh /etc/profile.d/
ADD chruby.sh /etc/drone.d/
RUN ruby-install ruby 2.2.2
