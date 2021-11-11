FROM ubuntu:16.04
MAINTAINER "Dave Scott McCarthy <dave@aslittledesign.com>"

# Ignore TTY warnings on install
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && \
    apt-get install -y -qq \
            apt-utils \
            build-essential \
            patch \
            curl \
            git \
            ssh \
            vim \
            imagemagick \
            libmagickwand-dev \
            libcurl4-openssl-dev \
            libssl-dev \
            libreadline-dev \
            libsqlite3-dev

# Set Ruby Version environment variable
ENV RUBY_VERSION 2.3.0

# Install Ruby
RUN echo 'gem: --no-document' >> /usr/local/etc/gemrc &&\
    mkdir /src && cd /src && git clone https://github.com/sstephenson/ruby-build.git &&\
    cd /src/ruby-build && ./install.sh &&\
    cd / && rm -rf /src/ruby-build && ruby-build $RUBY_VERSION /usr/local

RUN gem update --system &&\
    gem install bundler
