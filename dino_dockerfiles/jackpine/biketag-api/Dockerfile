FROM phusion/passenger-ruby22:latest
MAINTAINER Michael Kirk <michael@jackpine.me>

ENV HOME /root

CMD ["/sbin/my_init"]

# Phusion hasn't updated their images lately.
# Lifted this update oneliner from https://github.com/phusion/passenger-docker/issues/125
RUN apt-get update \
      && apt-get upgrade -y \
      && apt-get install -y ruby2.3 ruby2.3-dev \
      && ruby-switch --set ruby2.3 \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*

RUN gem install bundler

RUN rm /etc/service/nginx/down
RUN rm /etc/nginx/sites-enabled/default

ADD config/containers/api/conf/biketag-api.conf /etc/nginx/sites-enabled/biketag-api.conf

# Don't re-run bundle install unless Gemfile changes - otherwise if we do it
# *after* we add the app, we'll run bundle install everytime any file in the
# app changes.  Copy the Gemfile and Gemfile.lock into the image.
# Temporarily set the working directory to where they are.
WORKDIR /tmp
ADD Gemfile /tmp/Gemfile
ADD Gemfile.lock /tmp/Gemfile.lock
RUN bundle install

ADD . /home/app/biketag-api

# Script to copy mounted env secrets
RUN mkdir -p /etc/my_init.d
ADD config/containers/api/conf/distribute-secrets.sh /etc/my_init.d/10-distribute-secrets.sh

RUN chown -R app:app /home/app/biketag-api

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

