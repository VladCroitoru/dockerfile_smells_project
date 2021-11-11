# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:latest

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y wget openjdk-8-jre
RUN mkdir -p /opt/hue2mqtt
RUN wget https://github.com/owagner/hue2mqtt/releases/download/v0.12/hue2mqtt.jar -O /opt/hue2mqtt/hue2mqtt.jar
RUN mkdir /etc/service/hue2mqtt
COPY hue2mqtt.sh /etc/service/hue2mqtt/run
RUN chmod +x /etc/service/hue2mqtt/run

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
