# https://hub.docker.com/r/nodesource/jessie/tags/
FROM nodesource/jessie:6.7.0

MAINTAINER Marco Raddatz

# Debugging helpers
RUN alias ll='ls -alG'

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

# Install tools
RUN apt-get update; \
    apt-get install -y apt-utils apt-transport-https; \
    apt-get install -y locales curl wget; \
    apt-get install -y libnss-mdns avahi-discover libavahi-compat-libdnssd-dev libkrb5-dev; \
    apt-get install -y nano vim

# Install Homebridge
#RUN npm install -g homebridge --unsafe-perm
RUN npm install -g hap-nodejs@0.4.24 --unsafe-perm
RUN npm install -g homebridge@0.4.19 --unsafe-perm

# Final settings
COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf

USER root
RUN mkdir -p /var/run/dbus

ADD image/run.sh /root/run.sh

# Run container
EXPOSE 5353 51826
CMD ["/root/run.sh"]
