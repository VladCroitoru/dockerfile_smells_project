#FROM phusion/baseimage:0.9.15
FROM teamworksi/base-image:0.9.18
MAINTAINER "Raphaël Charrat <no-reply@teamwork.net>"

ENV APACHE_RUN_USER www-data \
    APACHE_RUN_GROUP www-data \
    APACHE_LOG_DIR /var/log/apache2


# Manually set the apache environment variables in order to get apache to work immediately.
RUN echo www-data > /etc/container_environment/APACHE_RUN_USER && \
  echo www-data > /etc/container_environment/APACHE_RUN_GROUP && \
  echo /var/log/apache2 > /etc/container_environment/APACHE_LOG_DIR && \
  echo /var/lock/apache2 > /etc/container_environment/APACHE_LOCK_DIR && \
  echo /var/run/apache2.pid > /etc/container_environment/APACHE_PID_FILE && \
  apt-get update && apt-get -y upgrade && \
  apt-get install -y apache2 php5-gd unzip \
	libicu-dev unzip zlib1g-dev php5-intl php5 \
  software-properties-common \
	libapache2-mod-php5 php5-cli php-soap php5-mcrypt \
	php5-mysqlnd php5-ldap apache2-utils graphviz && \
	php5enmod mcrypt && \
	php5enmod mysql && \
	php5enmod ldap && \
	a2enmod rewrite && \
  add-apt-repository -y ppa:ansible/ansible && \
  apt-get update && \
  apt-get install -y ansible && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  chown -R www-data: /var/www/html

VOLUME "/var/www/html"


ADD config/apache/000-default.conf /etc/apache2/sites-available/000-default.conf
ADD service /etc/service
ADD config/ansible /etc/ansible
ADD bug_fixes /bug_fixes
ADD tools /tools

RUN chmod +x /etc/service/apache/run && \
    chmod +x /etc/service/firstrun/run && \
    chmod +x /tools/*.sh


EXPOSE 80

CMD ["/sbin/my_init"]
