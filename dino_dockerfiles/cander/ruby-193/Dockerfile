# This is an Ubuntu 14:04 image for doing development on Rails 4.1.x application under Ruby 1.9.3
# It includes some extra packages we use in our app, and everything is left
# installed in the image - i.e., no effort has been made to clean up any
# packages after the initial install to reduce the image size.

FROM ubuntu:14.04
MAINTAINER Charles Anderson "master.sparkle@gmail.com"
ENV REFRESHED_AT 2016-10-17

# basic packages for Ruby development with native extensions
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    git build-essential ruby1.9.3 ruby-dev build-essential

# extra packages our gems use
RUN apt-get install -y libqrencode-dev libxml2-dev libxslt1-dev \
            libmysqlclient-dev imagemagick

# our current version of Bundler
RUN gem install bundler --no-ri --no-rdoc --version 1.11.2

# TODO: install rbenv to allow for picking and choosing Rubies

# given our Gemfile, make sure we can install all gems
# WORKDIR /tmp/app
# ADD Gemfile /tmp/app
# ADD Gemfile.lock /tmp/app
# RUN bundle install --path vendor/bundle --without development test
