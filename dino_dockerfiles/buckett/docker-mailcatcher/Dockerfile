# MailCatcher Dockerfile
#
# https://github.com/buckett/docker-mailcatcher
#
# Pull base image (nice and small).

FROM debian:jessie

MAINTAINER Matthew Buckett <matthew.buckett@it.ox.ac.uk>

# Install stuff for doing ruby development and building mailcatcher.
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y ruby ruby-dev make g++ libsqlite3-0 libsqlite3-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* 

RUN \
  # Doesn't work with newer versions of i18n
  # https://github.com/sj26/mailcatcher/issues/155
  gem install i18n -v 0.6.11 --no-rdoc --no-ri && \
  gem install mailcatcher --no-rdoc --no-ri

EXPOSE 1025
EXPOSE 1080

# Allocate a terminal, otherwise it backgrounds and docker exit
# Listening on localhost inside a container isn't very useful
CMD ["mailcatcher", "-f", "--ip", "0.0.0.0"]



