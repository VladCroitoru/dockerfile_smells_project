FROM php:7.0-apache

MAINTAINER "Gary Smith" <docker@kc.gs>

RUN apt-get update && apt-get install -y \
	curl \
	lynx-cur \
    libmcrypt-dev \
	libcurl4-gnutls-dev \
	libxml2-dev \
	libbz2-dev \
	re2c \
    libvpx-dev \
    zlib1g-dev \
    libgd-dev \
    libssl-dev \
    libtidy-dev \
    libxslt1-dev \
    libexif-dev \
    libssh2-1-dev \
	libsqlite3-dev

RUN docker-php-ext-install json \
	&& docker-php-ext-install mbstring \
	&& docker-php-ext-install tokenizer \
    && docker-php-ext-install gd \
	&& docker-php-ext-install curl \
	&& docker-php-ext-install dom \
	&& docker-php-ext-install bz2 \
	&& docker-php-ext-install pcntl \
#	&& docker-php-ext-install odbc \
#	&& docker-php-ext-install sybase \
	&& docker-php-ext-install mysqli \
	&& docker-php-ext-install pdo \
	&& docker-php-ext-install pdo_mysql \
	&& docker-php-ext-install pdo_sqlite \
	&& docker-php-ext-install phar \
	&& docker-php-ext-install posix \
	&& docker-php-ext-install simplexml \
	&& docker-php-ext-install soap \
	&& docker-php-ext-install sockets \
	&& docker-php-ext-install tidy \
	&& docker-php-ext-install zip \
	&& docker-php-ext-install bcmath \
	&& docker-php-ext-install calendar \
	&& docker-php-ext-install ctype \
	&& docker-php-ext-install exif \
 	&& rm -rf /var/lib/apt/lists/*
	
RUN a2enmod rewrite \
	&& a2enmod ssl \
	&& a2enmod vhost_alias

# Update the PHP.ini file, enable <? ?> tags and quieten logging.
# RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" 	/usr/local/etc/php/php.ini
# RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" 	/usr/local/etc/php/php.ini

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

RUN service apache2 restart

