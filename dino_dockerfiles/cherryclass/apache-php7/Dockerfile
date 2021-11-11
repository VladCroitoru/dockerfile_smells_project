FROM debian:stretch-slim
MAINTAINER M. Frébourg
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install \
apache2 \
php7.0 \
curl \
lynx-cur \
libapache2-mod-php7.0 \
php7.0-fpm \
php7.0-mysql \
php7.0-curl \
php7.0-json \
php7.0-gd \
php7.0-mcrypt \
php7.0-msgpack \
php7.0-memcached \
php7.0-intl \
php7.0-sqlite3 \
php7.0-gmp \
php7.0-geoip \
php7.0-mbstring \
php7.0-xml \
php7.0-zip \
composer \
mcrypt \
sudo \
nano \
ssh \
python-certbot-apache \
php-smbclient \
php-net-socket \
php-apcu


# Enable apache mods.
RUN a2enmod php7.0
RUN a2enmod rewrite
RUN a2enmod proxy_fcgi setenvif
RUN a2enconf php7.0-fpm
RUN a2enmod expires
RUN a2enmod ext_filter
RUN a2enmod headers

ADD php.ini /etc/php/7.0/apache2/php.ini

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

RUN mkdir var/www/adminer/
ADD index.php var/www/index.php
ADD adminer-4.3.1-mysql.php var/www/adminer/index.php
ADD adminer.conf /etc/apache2/sites-available/adminer.conf
RUN a2ensite adminer.conf

RUN chown -R www-data:www-data /var/www
RUN chsh -s /bin/bash www-data
RUN adduser www-data sudo

EXPOSE 80 443 22 25 

# By default start up apache in the foreground, override with /bin/bash for interative.
CMD /usr/sbin/apache2ctl -D FOREGROUND

#sudo certbot --authenticator webroot --installer apache --webroot-path /var/www/adminer -d adminer.cherryclass.net -d www.adminer.cherryclass.net

#apt install phpmyadmin
# sudo nano /etc/phpmyadmin/config-db.php
#cd /var/www/html/example.org/public_html
#sudo ln -s /usr/share/phpmyadmin
#/etc/phpmyadmin/config.inc.php Server(s) configuration->>> $cfg['ForceSSL'] = 'true';
