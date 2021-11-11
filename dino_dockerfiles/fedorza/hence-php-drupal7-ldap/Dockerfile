FROM hence/php-drupal7
MAINTAINER Fedor Zakharov <fedor@therefore.ca>

ENV PHP_PM_MAX_CHILDREN=200\
	PHP_PM_MIN_SPARE_SERVERS=20\
	PHP_PM_MAX_SPARE_SERVERS=100

RUN apk --update add openldap-clients  &&  \
touch /etc/openldap/ldap.conf  &&  \
echo "TLS_CACERT  /etc/ssl/certs/joinedcert_547050.pem" > /etc/openldap/ldap.conf