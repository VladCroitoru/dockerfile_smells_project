FROM ubuntu:14.04

# add sources
RUN echo 'deb http://download.videolan.org/pub/debian/stable/ /' >> /etc/apt/sources.list
RUN echo 'deb-src http://download.videolan.org/pub/debian/stable/ /' >> /etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main multiverse' >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get -y upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install wget inotify-tools
RUN wget -O - https://download.videolan.org/pub/debian/videolan-apt.asc|sudo apt-key add -
RUN apt-get update

# Need this environment variable otherwise mysql will prompt for passwords
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server apache2 wget php5 php5-json php5-curl php5-mysqlnd pwgen lame libvorbis-dev vorbis-tools flac libmp3lame-dev libavcodec-extra* libfaac-dev libtheora-dev libvpx-dev libav-tools git libgd3 libpng-dev libjpeg-dev libfreetype6-dev

# Install and Test PHP
RUN apt-get install --no-install-recommends -y \
		php5-cli \
		php5-dev \
		php5-json \
		php5-mysql php5-pgsql \
		php5-ldap \
		php5-imagick php5-gd php5-exactimage \
		php5-oauth \
		php5-xsl \
		php5-xmlrpc \
		php-pear && \
		php --version && \
		php -m

# Tidy up
RUN apt-get -y autoremove && apt-get clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install composer for dependency management
RUN php -r "readfile('https://getcomposer.org/installer');" | php && \
    mv composer.phar /usr/local/bin/composer

# download latest develop branch of ampache
ADD https://github.com/ampache/ampache/archive/develop.tar.gz /opt/develop.tar.gz

# extraction / installation
RUN rm -rf /var/www/* && \
    tar -C /var/www -xf /opt/develop.tar.gz ampache-develop --strip=1 && \
    cd /var/www && composer install --prefer-source --no-interaction && \
    chown -R www-data /var/www

# copy defaults (install.lib.php file)
ADD install.lib.php /install.lib.php
RUN cp /install.lib.php /var/www/lib/install.lib.php
RUN rm /install.lib.php

# setup mysql like this project does it: https://github.com/tutumcloud/tutum-docker-mysql
# Remove pre-installed database

RUN rm -rf /var/lib/mysql/*
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ENV MYSQL_PASS **Random**
# Add VOLUMEs to allow backup of config and databases
VOLUME  ["/etc/mysql", "/var/lib/mysql"]

# setup apache with default ampache vhost
ADD 001-ampache.conf /etc/apache2/sites-available/
RUN rm -rf /etc/apache2/sites-enabled/*
RUN ln -s /etc/apache2/sites-available/001-ampache.conf /etc/apache2/sites-enabled/
RUN a2enmod rewrite

# Add job to cron to clean the library every night
RUN echo '30 7    * * *   www-data php /var/www/bin/catalog_update.inc' >> /etc/crontab

VOLUME ["/media"]
VOLUME ["/var/www/config"]
VOLUME ["/var/www/themes"]
EXPOSE 80

CMD ["/run.sh"]
