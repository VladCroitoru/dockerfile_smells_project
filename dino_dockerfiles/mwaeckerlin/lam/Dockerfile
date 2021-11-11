# ubuntu xenial dropped php5 and installs php7
# ldap-account-manager supports php7 with release 5.3
# currently xenial provides ldap-account-manager 5.2
# last check: 2018-01-11
FROM ubuntu:trusty
ADD start.sh /start.sh
CMD /start.sh
ADD health.sh /health.sh
HEALTHCHECK --interval=60s --timeout=30s --start-period=600s --retries=3 CMD /health.sh
#FROM mwaeckerlin/ubuntu-base
MAINTAINER mwaeckerlin

ENV CONFIG=/etc/ldap-account-manager
ENV DATA=/var/lib/ldap-account-manager

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install --no-install-recommends --no-install-suggests -y ldap-account-manager php5-imap wget rsync \
 && php5enmod imap \
 && mv $CONFIG $CONFIG.original \
 && mv $DATA $DATA.original \
 && mkdir $DATA $CONFIG \
 && chown www-data.www-data $DATA $CONFIG \
 && sed -i 's,DocumentRoot .*,DocumentRoot /usr/share/ldap-account-manager,' /etc/apache2/sites-available/000-default.conf \
 && ln -sf /proc/1/fd/1 /var/log/apache2/access.log \
 && ln -sf /proc/1/fd/2 /var/log/apache2/error.log

EXPOSE 80
VOLUME $CONFIG
VOLUME $DATA
