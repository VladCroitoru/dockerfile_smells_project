FROM debian:wheezy

RUN apt-get update && apt-get -y install slapd ldap-utils

# Default configuration: can be overridden at the docker command line
ENV LDAP_ROOTPASS root
ENV LDAP_ORGANISATION Acme Widgets Inc.
ENV LDAP_DOMAIN example.com

RUN mkdir -p /slapd/init
ADD init/*.ldif /slapd/init/
VOLUME /var/lib/ldap
VOLUME /slapd/import.ldif

EXPOSE 389

ADD slapd.sh /slapd.sh
CMD ["/bin/sh", "/slapd.sh"]
