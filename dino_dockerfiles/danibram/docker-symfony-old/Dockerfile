FROM php:5.6-apache

RUN apt-get update \
    && apt-get install -y git libssl-dev zlib1g-dev libicu-dev g++ ruby-full build-essential \
    && pecl install xdebug \
    && echo zend_extension=xdebug.so > /usr/local/etc/php/conf.d/xdebug.ini \
    && pecl install apcu-beta \
    && echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini \
    && docker-php-ext-install zip mbstring intl

RUN apt-get autoclean

ADD app.conf /etc/apache2/sites-available/000-default.conf
RUN a2ensite 000-default

ADD ServerName.conf /etc/apache2/conf-available/ServerName.conf
RUN a2enconf ServerName

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

ADD php.ini /usr/local/etc/php/php.ini

RUN a2enmod rewrite

RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/bin/composer

RUN gem install compass

RUN usermod -u 1000 www-data

ONBUILD ADD . /var/www/html
ONBUILD RUN chown -R www-data:www-data .

WORKDIR /var/www/html