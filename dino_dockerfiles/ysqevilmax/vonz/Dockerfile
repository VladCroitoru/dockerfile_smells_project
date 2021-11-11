FROM php:5.6-apache

RUN apt-get update && apt-get install -y \
	bzip2 \
	libcurl4-openssl-dev \
	libfreetype6-dev \
	libicu-dev \
	libjpeg-dev \
	libmcrypt-dev \
	libmemcached-dev \
	libpng12-dev \
	libpq-dev \
	libxml2-dev \
	&& rm -rf /var/lib/apt/lists/*

# https://doc.owncloud.org/server/8.1/admin_manual/installation/source_installation.owncloud#prerequisites
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd exif intl mbstring mcrypt mysql opcache pdo_mysql pdo_pgsql pgsql zip

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

# PECL extensions
RUN pecl install APCu-4.0.10 redis memcached \
	&& docker-php-ext-enable apcu redis memcached

ENV OWNCLOUD_VERSION 9.1.0.5

ENV OWNCLOUD_TAG master

# Fetch ownCloud dist files 
ADD https://codeload.github.com/owncloud/core/tar.gz/${OWNCLOUD_TAG} \
    /tmp/owncloud.tar.gz
ADD https://codeload.github.com/owncloud/3rdparty/tar.gz/${OWNCLOUD_TAG} \
    /tmp/3rdparty.tar.gz

# Install ownCloud 
RUN tar -C /var/www/ -xvf /tmp/owncloud.tar.gz && \
    tar -C /var/www/ -xvf /tmp/3rdparty.tar.gz && \
    mv /var/www/core-${OWNCLOUD_TAG} /var/www/owncloud && \
    rmdir /var/www/owncloud/3rdparty && \
    mv /var/www/3rdparty-${OWNCLOUD_TAG} /var/www/owncloud/3rdparty && \
    rm /tmp/owncloud.tar.gz /tmp/3rdparty.tar.gz

WORKDIR /var/www/owncloud

# add my own configuration file
# ADD https://raw.githubusercontent.com/YsqEvilmax/vonz/master/setting.sh /setting.sh
COPY setting.sh /setting.sh
RUN chmod +x /setting.sh

# enable https, refer to https://github.com/docker-library/owncloud/issues/23
COPY owncloud-ssl.conf /etc/apache2/sites-available/

RUN a2enmod rewrite
RUN a2enmod ssl
RUN a2enmod headers
RUN a2ensite owncloud-ssl

EXPOSE 80 443 

ENTRYPOINT ["/setting.sh"]
CMD ["apache2-foreground"]


