FROM debian:jessie

MAINTAINER Richard Kovacs <kovacsricsi@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /etc/ldap && \
    mkdir -p /var/lib/ldap && \
    mkdir -p /run/slapd

RUN apt-get update && \
  apt-get -y install slapd ldap-utils ldapscripts && \
  rm -rf /var/lib/apt/lists/*

ADD ldapscripts/ /etc/ldapscripts/
ADD scripts /scripts
RUN chmod +x /scripts/start.sh
RUN touch /first_run

# Add VOLUMEs to allow backup of config, logs and databases
# * To store the data outside the container, mount /var/lib/ldap as a data volume
VOLUME ["/etc/ldap", "/var/lib/ldap", "/run/slapd"]
EXPOSE 389

# Kicking in
CMD ["/scripts/start.sh"]
