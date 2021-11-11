FROM phusion/baseimage:latest
MAINTAINER Eric Gazoni <eric@adimian.com>

ENV HOME /root

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Configure apt
RUN apt-get -y update

# Install slapd
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y slapd ldap-utils

# Default configuration: can be overridden at the docker command line
ENV LDAP_ROOTPASS toor
ENV LDAP_ORGANISATION Acme Widgets Inc.
ENV LDAP_DOMAIN example.com

EXPOSE 389

ADD slapd.sh /etc/service/slapd/run
RUN chmod +x /etc/service/slapd/run

ADD ldap-schema /tmp
RUN chmod +x /tmp/install-schema.sh
