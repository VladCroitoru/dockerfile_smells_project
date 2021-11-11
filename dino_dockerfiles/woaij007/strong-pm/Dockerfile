# Pull base image.
FROM strongloop/strong-pm

# File Author.
MAINTAINER Cola <cmao@worldelites.com>

USER root

RUN rm /etc/localtime && \
  ln -sf /usr/share/zoneinfo/US/Pacific /etc/localtime

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y pdftk imagemagick && \
  rm -rf /var/lib/apt/lists/*

USER strong-pm