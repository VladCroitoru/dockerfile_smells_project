FROM php:7.0-apache
MAINTAINER Ludwig Prager <ludwig.prager@celp.de>

RUN apt-get update

RUN apt-get install -q -y libpng12-dev imagemagick

RUN docker-php-ext-install gd

RUN apt-get install -q -y php-pear  php5-gd php5-sqlite poppler-utils catdoc

ADD misc/seeddms-quickstart-5.0.5.tar.gz /var/www/

RUN a2enmod rewrite

COPY misc/php.ini /usr/local/etc/php/
COPY misc/000-default.conf /etc/apache2/sites-available/

COPY misc/settings.xml /var/www/seeddms50x/seeddms-5.0.5/conf/settings.xml
RUN chown -R www-data:www-data /var/www/seeddms50x/

RUN touch /var/www/seeddms50x/seeddms-5.0.5/conf/ENABLE_INSTALL_TOOL
