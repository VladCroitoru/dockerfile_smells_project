FROM phusion/baseimage:0.9.8
MAINTAINER Birkan Duman <birkan.duman@gmail.com>

ENV HOME /root

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Configure apt
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise universe' >> /etc/apt/sources.list
RUN apt-get -y update

# Install slapd
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y slapd ldap-utils

# Default configuration: can be overridden at the docker command line
ENV LDAP_ROOTPASS toor
ENV LDAP_ORGANISATION Acme Widgets Inc.
ENV LDAP_DOMAIN example.com
ENV LDAP_BASE_DN dc=example,dc=com

EXPOSE 389

RUN mkdir /etc/service/slapd
#ADD slapd.sh /etc/service/slapd/run
COPY slapd.sh /usr/sbin/run

COPY config_password.ldif config_password.ldif
COPY ldap-db.ldif ldap-db.ldif
COPY lider_ahenk.ldif lider_ahenk.ldif
COPY load_ppolicy_modules.ldif load_ppolicy_modules.ldif
COPY test-data.ldif test-data.ldif

# To store the data outside the container, mount /var/lib/ldap as a data volume

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
CMD ["run"]

# vim:ts=8:noet:
