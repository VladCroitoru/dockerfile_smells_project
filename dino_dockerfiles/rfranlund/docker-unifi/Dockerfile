FROM debian:9

MAINTAINER Robert Frånlund <robert.franlund@poweruser.se>

ENV DEBIAN_FRONTEND noninteractive

# Install Unifi dependencies
RUN apt-get update && \
    apt-get --assume-yes --no-install-recommends install openjdk-8-jre-headless procps wget mongodb-server jsvc binutils curl logrotate

# Set URL for Unifi package
ARG PACKAGE_URL=https://dl.ui.com/unifi/6.2.26/unifi_sysvinit_all.deb

RUN wget -O /tmp/unifi_sysvinit_all.deb ${PACKAGE_URL} && \
    dpkg --install /tmp/unifi_sysvinit_all.deb && \
    rm -rf /tmp/unifi_sysvinit_all.deb /var/lib/unifi/*

# Expose ports
EXPOSE 8080/tcp 8443/tcp 8880/tcp 8843/tcp 3478/udp

# Add start script
# 2016-10-25 - Fixed strange Docker Hub bug
# https://forums.docker.com/t/automated-docker-build-fails/22831/27

ADD assets /assets
RUN mv /assets/start.sh / && rmdir /assets

VOLUME ["/var/lib/unifi"]

WORKDIR /var/lib/unifi

CMD ["/start.sh"]
