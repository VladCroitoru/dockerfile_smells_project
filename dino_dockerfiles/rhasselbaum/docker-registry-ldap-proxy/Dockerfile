# A Docker registry proxy that authenticates against LDAP for updates.

FROM ubuntu:14.04
MAINTAINER Rob Hasselbaum <rob@hasselbaum.met>

# Install Apache and the LDAP auth module. Enable required modules and disable default sites.
RUN DEBIAN_FRONTEND=noninteractive \
 apt-get update && \
 apt-get install -y apache2 libapache2-mod-webauthldap && \
 a2enmod ssl proxy proxy_http authnz_ldap headers && \
 a2dissite 000-default

# Install site.
COPY reg-proxy.conf /etc/apache2/sites-available/reg-proxy.conf
RUN a2ensite reg-proxy

# Volumes to contain certs and private keys.
VOLUME ["/etc/ssl/certs", "/etc/ssl/private"]

# Set up runtime
COPY start-apache2.sh /start-apache2.sh
RUN chmod a+x /start-apache2.sh
CMD ["/bin/bash", "/start-apache2.sh"]

# ENVIRONMENT VARIABLES. See README.md for descriptions.

ENV SERVER_NAME=localhost \
    LDAP_TRUSTED_GLOBAL_CERT_PATH=/etc/ssl/certs/ldap-ca-cert.pem \
    LDAP_LIBRARY_DEBUG=0 \
    SSL_CERTIFICATE_FILE=/etc/ssl/certs/reg-proxy-cert.pem \
    SSL_CERTIFICATE_KEY_FILE=/etc/ssl/private/reg-proxy-key.pem \
    AUTH_LDAP_URL="ldap://dc-01.example.com:3268/?userPrincipalName?sub" \
    LDAP_TRUSTED_MODE=TLS \
    REQUIRE_AUTHZ_TYPE=ldap-user \
    REQUIRE_AUTHZ_USERS=registry.admin@example.com \
    LOG_LEVEL=warn

