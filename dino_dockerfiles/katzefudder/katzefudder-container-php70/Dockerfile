FROM ubuntu:16.04

MAINTAINER Florian Dehn <flo@katzefudder.de>
LABEL Description="Frontend Server PHP" Vendor="katzefudder.de"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
	curl wget exim4 openssh-server ruby ruby-dev ruby-compass graphviz mysql-client sudo apt-utils \
	apache2 libapache2-mod-fcgid php php-curl php-common php-mbstring php-mcrypt php-gd php-xdebug php-intl php-mysql php-imap php-sqlite3 php-pear php-apcu \
&& apt-get clean

# * * * * * * * * * setup Apache
RUN chown www-data: /var/www -R && chmod -R 777 /var/www
ADD scripts/make_vhost.sh /tmp/
ADD scripts/vhost_template.txt /tmp/
RUN /tmp/make_vhost.sh docker-php /etc/apache2/sites-available/docker-php.conf

RUN a2enconf php7.0-fpm.conf && a2ensite docker-php.conf && a2dissite 000-default && a2enmod rewrite ssl && service php7.0-fpm start && mkdir -p /etc/apache2/ssl

# * * * * * * * * * add SSH public key
RUN mkdir /root/.ssh/ && chmod 700 /root/.ssh/
ADD keys/docker.pub /root/.ssh/docker.pub
RUN cat /root/.ssh/docker.pub >> /root/.ssh/authorized_keys && chmod 644 /root/.ssh/authorized_keys

# * * * * * * * * * generate SSL key
RUN openssl genrsa -out /etc/apache2/ssl/ssl.key 2048; \
	openssl req -new -x509 -key /etc/apache2/ssl/ssl.key -out /etc/apache2/ssl/ssl.crt -days 3650 -subj /CN=docker-php

# * * * * * * * * * set server name
RUN echo "ServerName docker.local" >> /etc/apache2/apache2.conf

# * * * * * * * * * install composer && nodejs
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer && curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install nodejs -y && npm install -g grunt-cli && npm install -g bower
RUN gem install compass

# * * * * * * * * * prepare directories
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/www/public

# * * * * * * * * * startup
COPY scripts/startup.sh /tmp/startup.sh
CMD ["/tmp/startup.sh"]

# * * * * * * * * * clean up
RUN rm -r /var/lib/apt/lists/*

WORKDIR /var/www

# * * * * * * * * * expose ports
EXPOSE 22 80 443

RUN a2enmod proxy_fcgi && a2dismod mpm_event && a2enmod mpm_prefork && service apache2 restart
EXPOSE 80