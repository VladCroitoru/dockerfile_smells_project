FROM seti/observium
MAINTAINER evanhoucke <emmanuel.vanhoucke@a-sis.com>

RUN apt-get update && \
    apt-get install php5-ldap && \
    a2enmod ldap auth_basic authnz_ldap authz_user

