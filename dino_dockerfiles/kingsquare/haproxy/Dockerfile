###
#
# A HAProxy container
#
# < 200MB image
# based off the dockerfile/haproxy image
###
FROM ubuntu:14.04
MAINTAINER Kingsquare <docker@kingsquare.nl>

####
# Install HAProxy
RUN sed -i 's/^# \(.*-backports\s\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get install -y --no-install-recommends haproxy=1.5.3-1~ubuntu14.04.1 && \
  sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy && \
  echo "" > /etc/haproxy/ssl.pem && \
  rm -rf /var/lib/apt/lists/*

####
# Add config
ADD resources/haproxy.cfg /etc/haproxy/haproxy.cfg
ADD resources/start.sh /start.sh

####
# Exose default ports
EXPOSE 80
EXPOSE 443

####
# Where to allow custom config
VOLUME ["/custom"]

####
# Default working directory
WORKDIR /etc/haproxy

####
# Run the application
CMD ["bash", "/start.sh"]
