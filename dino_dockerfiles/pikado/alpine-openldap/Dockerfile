FROM alpine
MAINTAINER Pika Do <pokido99@gmail.com>

# Proxy settings if necessary
# ENV http_proxy=http://proxy.mydomain.com:8080
# ENV https_proxy=http://proxy.mydomain.com:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Install OpenLDAP
RUN apk --no-cache --update add openldap openldap-clients

# Configure config database
ENV OPENLDAP_PASS_CONFIG config
RUN echo -e "database config\nrootdn \"cn=admin,cn=config\"\nrootpw $OPENLDAP_PASS_CONFIG" >> /etc/openldap/slapd.conf

EXPOSE 389

# Set default command
CMD ["slapd","-u","ldap","-g","ldap","-h","ldap:/// ldapi:///","-d","4"]
