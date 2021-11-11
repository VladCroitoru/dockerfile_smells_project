# Croodle Dockerfile.
#
# https://github.com/fuerst/croodle-docker
#
# Version 1.0

FROM php:7-apache
MAINTAINER Bernhard Fürst, bernhard.fuerst@fuerstnet.de

# You may overwrite the version.
# Use a release tag from https://github.com/jelhan/croodle/releases.
ENV CROODLE_VERSION v0.5.6

WORKDIR /var/www/html

# Grab and expand release files.
RUN rm -rf * \
  && curl -SL -o croodle.tgz https://github.com/jelhan/croodle/releases/download/${CROODLE_VERSION}/croodle-${CROODLE_VERSION}.tar.gz \
  && tar zxf croodle.tgz \
  && rm croodle.tgz \
  && chmod 777 data

# Install Cron
RUN apt-get update && apt-get -y install -qq cron
ADD crontab /etc/cron.d/croodle
RUN chmod 0644 /etc/cron.d/croodle
RUN crontab /etc/cron.d/croodle
