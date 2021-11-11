FROM php:7.1-apache
MAINTAINER broadiq <info@broadiq.com>

ENV SCRM_VERSION v7.10.10
#ENV SCRM_VERSION v7.11.7

# Install requirements
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get \
        install -y --no-install-recommends \
            libfreetype6-dev \
            libjpeg62-turbo-dev \
            libmcrypt-dev \
            libcurl4-openssl-dev \
            libssl-dev \
            libpng-dev \
            libpq-dev \
            libxml2-dev \
            zlib1g-dev \
            libc-client-dev \
            libkrb5-dev \
            libldap2-dev \
            cron \
            git \
            busybox

# Busybox installation
RUN busybox --install

# Docker image configuration
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
    && docker-php-ext-install -j$(nproc) iconv \
		    mcrypt \
				pdo_mysql \
        curl \
        mbstring \
        mysqli \
        zip \
        ftp \
        pdo_pgsql \
        gd \
        fileinfo \
        soap \
        zip \
        imap \
        ldap

WORKDIR /var/www/html

#Setting UP SuiteCRM
RUN curl https://codeload.github.com/salesagility/SuiteCRM/tar.gz/${SCRM_VERSION} | tar xzv --strip 1

#Setting Up config file redirect for proper use with docker volumes
RUN mkdir conf.d \
    && touch conf.d/config.php conf.d/config_override.php \
    && ln -s conf.d/config.php \
    && ln -s conf.d/config_override.php

RUN (crontab -l 2>/dev/null; echo "* * * * *  php -f /var/www/html/cron.php > /dev/null 2>&1 ") | crontab -

# composer
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');"
RUN php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
RUN composer install --no-plugins --no-scripts

# bootstrap files
RUN mkdir /bootstrap
COPY php.custom.ini /usr/local/etc/php/conf.d/
COPY init.sh /bootstrap/init.sh
COPY config.php ./conf.d

# clean temporary files and packages
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN chown -R www-data:www-data . && chmod -R 755 .


VOLUME [ "/var/www/html/upload", "/var/www/html/conf.d" ]

EXPOSE 80

CMD ["/bootstrap/init.sh"]

# End of file
# vim: set ts=2 sw=2 noet:

