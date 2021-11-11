#
# Based on a Ruby Dockerfile
#
# https://github.com/dockerfile/ruby
#

# Pull base image.
FROM ubuntu:16.04

# Install Ruby.
RUN \
  apt-get update && \
  apt-get install -y git nodejs openssl make gcc g++ zlib1g-dev ruby rake ruby-dev ruby-bundler libruby2.3 && \
  rm -rf /var/lib/apt/lists/*

RUN mkdir /app
RUN chown -R nobody:nogroup /app

ADD Gemfile /app
ADD Gemfile.lock /app

RUN cd /app && bundle install

# Define working directory.
WORKDIR /app
