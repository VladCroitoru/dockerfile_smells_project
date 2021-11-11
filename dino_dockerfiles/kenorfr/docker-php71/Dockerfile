FROM php:7.1-fpm
WORKDIR "/application"

ENV DEBIAN_FRONTEND noninteractive

# location : /usr/local/bin/
RUN chmod -R 700 /usr/local/bin/

# Locales
RUN apt-get update \
	&& apt-get install -y locales

RUN dpkg-reconfigure locales \
	&& locale-gen C.UTF-8 \
	&& /usr/sbin/update-locale LANG=C.UTF-8

RUN echo 'fr_FR.UTF-8 UTF-8' >> /etc/locale.gen \
	&& locale-gen

ENV LC_ALL C.UTF-8
ENV LANG fr_FR.UTF-8
ENV LANGUAGE fr_FR.UTF-8

# Common
RUN apt-get update \
	&& apt-get install -y \
		openssl \
		git

# PHP
# location php.ini : /usr/local/etc/php/conf.d/docker-php.ini

# intl
RUN apt-get update \
	&& apt-get install -y libicu-dev \
	&& docker-php-ext-configure intl \
	&& docker-php-ext-install intl

# xml
RUN apt-get update \
	&& apt-get install -y \
	libxml2-dev \
	libxslt-dev \
	&& docker-php-ext-install \
		dom \
		xmlrpc \
		xsl

# supervisor
# location : /etc/supervisor/conf.d/supervisord.conf
RUN apt-get update \
	&& apt-get install -y \
	supervisor

# images
RUN apt-get update \
	&& apt-get install -y \
	libfreetype6-dev \
	libjpeg62-turbo-dev \
	libpng12-dev \
	libgd-dev \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install \
		gd \
		exif

# database
RUN docker-php-ext-install \
	mysqli \
	pdo \
	pdo_mysql

# mcrypt
RUN apt-get update \
	&& apt-get install -y libmcrypt-dev \
	&& docker-php-ext-install mcrypt

# strings
RUN docker-php-ext-install \
	gettext \
	mbstring

# math
RUN apt-get update \
	&& apt-get install -y libgmp-dev \
	&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \
	&& docker-php-ext-install \
		gmp \
		bcmath

# compression
RUN apt-get update \
	&& apt-get install -y \
	libbz2-dev \
	zlib1g-dev \
	&& docker-php-ext-install \
		zip \
		bz2

# ftp
RUN apt-get update \
	&& apt-get install -y \
	libssl-dev \
	&& docker-php-ext-install \
		ftp

# ssh2
RUN apt-get update \
	&& apt-get install -y \
	libssh2-1-dev

# others
RUN docker-php-ext-install \
	soap \
	sockets \
	calendar \
	sysvmsg \
	sysvsem \
	sysvshm

# Install composer and put binary into $PATH
RUN curl -sS https://getcomposer.org/installer | php \
	&& mv composer.phar /usr/local/bin/ \
	&& ln -s /usr/local/bin/composer.phar /usr/local/bin/composer

## NodeJS
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
	&& apt-get install -y nodejs

# Clean
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*
