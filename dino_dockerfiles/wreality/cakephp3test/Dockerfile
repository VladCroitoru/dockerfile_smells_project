FROM php:7.2-apache
MAINTAINER Brian Adams <wreality@gmail.com>

#update apt-get
RUN apt-get update
#install the required components
RUN apt-cache search libjpeg
RUN apt-get install -y --no-install-recommends \
    libmcrypt-dev \
    g++ \
    libicu-dev \
    libmcrypt4 \
    libicu57 \
    zlib1g-dev \
    git \
    libxml2-dev \
    openssh-client \
    mysql-client \
    libjpeg62-turbo \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libzip-dev \
    libjpeg-dev \
    libpq-dev \
    libmcrypt-dev \
    libpng16-16
#install the PHP extensions we need
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
	docker-php-ext-install -j "$(nproc)" \
		gd \
		opcache \
		pdo_mysql \
		zip \
		intl \
                soap \
                mbstring 

#cleanup after the installations
RUN apt-get purge --auto-remove -y \
    libmcrypt-dev \
    g++ \
    libicu-dev \ 
    zlib1g-dev \ 
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libzip-dev \
    libjpeg-dev \
    libpq-dev \
    libmcrypt-dev 

#delete the lists for apt-get as the take up space we do not need.
RUN rm -rf /var/lib/apt/lists/*

#install composer globally so that you can call composer directly
RUN curl -sSL https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# install xdebug for code coverage
RUN curl -L -o /tmp/xdebug-2.6.1.tgz http://xdebug.org/files/xdebug-2.6.1.tgz \
    && tar xfz /tmp/xdebug-2.6.1.tgz \
        && rm -r /tmp/xdebug-2.6.1.tgz \
        && docker-php-source extract \
            && mv xdebug-2.6.1 /usr/src/php/ext/xdebug \
                && docker-php-ext-install xdebug \
                && docker-php-source delete

# enable apache rewrite
RUN a2enmod rewrite

# set www permissions
RUN usermod -u 1000 www-data

