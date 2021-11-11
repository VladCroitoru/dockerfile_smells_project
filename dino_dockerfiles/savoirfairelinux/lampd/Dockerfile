# docker Drupal
FROM    phusion/baseimage:18.04-1.0.0
MAINTAINER Mohammed Raza <mohammed.raza@savoirfairelinux.com>

# Set correct environment variables.
ENV HOME /root

RUN rm -f /etc/service/sshd/down
# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Update software source
RUN apt-get update

# Install Apache, MySQL, PHP, and others..
RUN apt install apt-transport-https lsb-release ca-certificates
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install wget git mysql-client mysql-server apache2 libapache2-mod-php7.2 pwgen python-setuptools php7.2-sqlite php7.2-mysql php-apc php7.2-gd php7.2-curl php7.2-memcache memcached mc php-pear php7.2-imagick php7.2-dev build-essential asciidoctor sendmail fabric npm nodejs-legacy

# Install drush, phpmd, phpcpd, site_audit, uploadprogress, behat, drupal_extension
RUN pear channel-discover pear.phpmd.org && pear channel-discover 'pear.pdepend.org' && pear install --alldeps 'phpmd/PHP_PMD'
RUN wget https://phar.phpunit.de/phpcpd.phar && chmod +x phpcpd.phar && mv phpcpd.phar /usr/local/bin/phpcpd
RUN pecl install -Z uploadprogress && echo "extension=uploadprogress.so" >> /etc/php7.2/apache2/conf.d/uploadprogress.ini && ln -s /etc/php7.2/mods-available/uploadprogress.ini /etc/php7.2/apache2/conf.d/20-uploadprogress.ini
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer && mkdir /opt/drupalextension && mkdir /opt/drush
COPY drupal-extension-composer.json /opt/drupalextension/composer.json
RUN cd /opt/drupalextension/ && composer install && ln -s /opt/drupalextension/bin/behat /usr/local/bin/behat
COPY drush-composer.json /opt/drush/composer.json
RUN cd /opt/drush && composer install && ln -s /opt/drush/bin/drush /usr/local/bin/drush && drush dl site_audit registry_rebuild-7.x -y
RUN cd /root/.drush && git clone https://github.com/sfl-drupal/po-import.git && /opt/drush/bin/drush cc drush

# Make mysql listen on the outside
RUN sed -i "s/^bind-address/#bind-address/" /etc/mysql/my.cnf

# Adding additional memcached daemon
RUN mkdir /etc/service/memcached
ADD service/memcached.sh /etc/service/memcached/run

# Adding additional mysqld daemon
RUN mkdir /etc/service/apache2
ADD service/apache2.sh /etc/service/apache2/run

# Adding additional apache2 daemon
RUN mkdir /etc/service/mysqld
ADD service/mysqld.sh /etc/service/mysqld/run

# Expose port 80 for apache connection on the aoutside
EXPOSE 80

# Clean up APT when done.
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
