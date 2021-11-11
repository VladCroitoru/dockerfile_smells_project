FROM ubuntu:14.04

MAINTAINER Maksym Nebot, <maksym.nebot@accenture.com>

#ENV VARIABLES

ENV LDAP_LTB_URL "ldap://ldap:389"
ENV LDAP_LTB_DN "cn=admin,dc=ldap,dc=example,dc=com"
ENV LDAP_LTB_PWD "changeme"
ENV LDAP_LTB_BS "dc=ldap,dc=example,dc=com"

# Install Apache2, PHP and LTB ssp
RUN apt-get update && apt-get install -y apache2 php5 php5-mcrypt php5-ldap curl && apt-get clean
RUN curl https://ltb-project.org/archives/self-service-password_0.9-1_all.deb > self-service-password.deb && dpkg -i self-service-password.deb ; rm -f self-service-password.deb

# Configure self-service-password site
RUN ln -s self-service-password /etc/apache2/sites-available/self-service-password.conf
RUN ln -s ../../mods-available/mcrypt.ini /etc/php5/apache2/conf.d/20-mcrypt.ini
RUN a2dissite 000-default && a2ensite self-service-password

# This is where configuration goes
ADD assets/config.inc.php /usr/share/self-service-password/conf/config.inc.php

RUN mkdir -p /etc/service/apache2
ADD assets/apache2.sh /etc/service/apache2/run
CMD ["/etc/service/apache2/run"]
EXPOSE 80
