# A Docker registry2 proxy that authenticates against LDAP.
FROM centos
MAINTAINER Dario Alves Junior <darioajr@gmail.com>

# Install Apache and the LDAP and SSL modules.
RUN yum --setopt=tsflags=nodocs -y install httpd mod_ssl mod_ldap openssl

# Clean installation caches
RUN rm -rf /var/cache/yum/*
RUN yum clean all

# Include conf files
ADD apache/reg2proxy.conf /etc/httpd/conf/reg2proxy.conf

# Include execution script
ADD docker_entrypoint.sh /docker_entrypoint.sh

# Configure Apache
RUN cat /etc/httpd/conf/reg2proxy.conf >> /etc/httpd/conf/httpd.conf
 

# Volume to certs and private keys.
VOLUME [ "/etc/httpd/ssl" ]

# Volume to logs
VOLUME [ "/var/log/httpd" ]


# Set up runtime
#COPY docker_entrypoint.sh /docker_entrypoint.sh
RUN chmod a+x /docker_entrypoint.sh
CMD ["/bin/bash", "/docker_entrypoint.sh"]

# ENVIRONMENT VARIABLES. See README.md for descriptions.

ENV SERVER_NAME=localhost \
    SSL_CERTIFICATE_FILE=/etc/ssl/certs/reg-proxy-cert.pem \
    SSL_CERTIFICATE_KEY_FILE=/etc/ssl/private/reg-proxy-key.pem \
    LDAP_TRUSTED_MODE=NONE \
    REQUIRE_AUTHZ_TYPE=ldap-user \
    REQUIRE_AUTHZ_USERS=registry.admin@example.com \
    LOG_LEVEL=warn \
    AUTH_NAME=MYDOMAIN \
    AUTH_LDAP_URL="ldap://yourdomain:3268/DC=youdomain,DC=local?sAMAccountName?sub?(&(objectCategory=User)(!(objectClass=contact))(!(userAccountControl:1.2.840.113556.1.4.803:=2)))" \
    AUTH_LDAP_BIND_DN="CN=youruser,OU=etc,DC=yourdomain,DC=local" \
    AUTH_LDAP_BIND_PASSWORD=yourpassword \
    REQUIRE_AUTHZ_GROUP="cn=yourgroup,OU=etc,DC=yourdomain,DC=local" \
    REGISTRY_PORT_5000_TCP_ADDR=localhost \
    REGISTRY_PORT_5000_TCP_PORT=5000

