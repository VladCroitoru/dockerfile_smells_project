FROM i386/ubuntu:12.04

MAINTAINER Mikhail Snetkov "ufoproger@gmail.com"
ENV DEBIAN_FRONTEND noninteractive

# Ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

# Deny restarting applications when installing them
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && chmod +x /usr/sbin/policy-rc.d

# Update system
RUN apt-get update && apt-get dist-upgrade -y

# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for debugging the container.
RUN apt-get -y install apache2 libapache2-mod-php5 php5-mcrypt php5-cli php5-common php5-json php5-memcache php5-mysql php5-gd php-pear php-apc php5-dev php5-curl curl git supervisor make

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pecl install uploadprogress

ENV COMPOSER_ALLOW_SUPERUSER	1
ENV COMPOSER_NO_INTERACTION		1

RUN /usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php
RUN /bin/mv composer.phar /usr/local/bin/composer
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Composer and Drush
RUN /usr/local/bin/composer self-update
RUN /usr/local/bin/composer global require drush/drush:6.*
RUN ln -s /.composer/vendor/drush/drush/drush /usr/local/bin/drush

# Enable apache mods.
RUN a2enmod php5
RUN a2enmod rewrite

# PHP
RUN sed -i 's/memory_limit = .*/memory_limit = 196M/' /etc/php5/apache2/php.ini
RUN sed -i 's/cgi.fix_pathinfo = .*/cgi.fix_pathinfo = 0/' /etc/php5/apache2/php.ini
RUN sed -i 's/upload_max_filesize = .*/upload_max_filesize = 512M/' /etc/php5/apache2/php.ini
RUN sed -i 's/post_max_size = .*/post_max_size = 512M/' /etc/php5/apache2/php.ini

RUN echo "extension=uploadprogress.so" > /etc/php5/conf.d/uploadprogress.ini

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/supervisor
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV SERVER_ADMIN_EMAIL admin@localhost

RUN usermod -u 1000 www-data
RUN usermod -a -G users www-data
RUN chown -R www-data:www-data /var/www

EXPOSE 80
WORKDIR /var/www
VOLUME ["/var/www"]
CMD ["/usr/bin/supervisord", "-n"]

# Add files
ADD ./config/supervisord-apache.conf /etc/supervisor/conf.d/supervisord-apache.conf
ADD ./config/apache-config.conf /etc/apache2/sites-enabled/000-default