FROM php:5.6-apache

RUN apt-get update && apt-get install -y \
        aria2 \
        unzip \
        python \
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
	sqlite3 \
	libsqlite3-dev \
	libbz2-dev \
        && rm -rf /var/lib/apt/lists/*

# https://doc.owncloud.org/server/latest/admin_manual/installation/source_installation.html
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd zip pdo_mysql pgsql bz2 intl mcrypt exif opcache
#	&& docker-php-ext-install ctype dom iconv json libxml posix simplexml xmlwriter zip zlib pdo_sqlite pdo_mysql pgsql curl fileinfo bz2 intl mcrypt openssl exif mbstring opcache pcntl
#	&& docker-php-ext-install gd exif intl mbstring mcrypt mysql opcache pdo_mysql pdo_pgsql pgsql zip pcntl
#	&& docker-php-ext-install ctype gd dom iconv json libxml posix simplexml xmlwriter zip zlib pdo_sqlite pdo_mysql pgsql curl fileinfo bz2 intl mcrypt openssl exif mbstring opcache && docker-php-ext-install ctype dom iconv json libxml posix simplexml xmlwriter zip zlib sqlite pdo_mysql pgsql curl fileinfo bz2 intl mcrypt openssl exif mbstring opcache pcntl

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
RUN pecl install APCu-4.0.11 redis memcached \
	&& docker-php-ext-enable apcu redis memcached

RUN a2enmod rewrite

ENV OWNCLOUD_VERSION 9.1.4

RUN curl -fsSL -o owncloud.tar.bz2 \
		"https://download.owncloud.org/community/owncloud-${OWNCLOUD_VERSION}.tar.bz2" \
	&& curl -fsSL -o owncloud.tar.bz2.asc \
		"https://download.owncloud.org/community/owncloud-${OWNCLOUD_VERSION}.tar.bz2.asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys E3036906AD9F30807351FAC32D5D5E97F6978A26 \
	&& gpg --batch --verify owncloud.tar.bz2.asc owncloud.tar.bz2 \
	&& rm -r "$GNUPGHOME" owncloud.tar.bz2.asc \
	&& tar -xjf owncloud.tar.bz2 -C /usr/src/ \
	&& rm owncloud.tar.bz2
# gpg key from https://owncloud.org/owncloud.asc

# Rename dirctory to appid & enable ocdownloader by default
RUN curl -fsSL -o oc.zip \
                "https://github.com/DjazzLab/ocdownloader/archive/master.zip" \
        && rm -rf /dev/shm/ocdownloader-master \
        && unzip oc.zip -d /dev/shm \
        && sed -i 's|</id>|</id><default_enable/>|' /dev/shm/ocdownloader-master/appinfo/info.xml \
        && mv /dev/shm/ocdownloader-master /usr/src/owncloud/apps/ocdownloader \
        && rm oc.zip

# Download latest youtube-dl binary, need python runtime
RUN curl -sSL https://yt-dl.org/latest/youtube-dl -o /usr/local/bin/youtube-dl && \
        chmod a+rx /usr/local/bin/youtube-dl

RUN cd /var/www/html && tar cf - --one-file-system -C /usr/src/owncloud . | tar xf - && chown -R www-data:www-data .

# Add user aria2 and fix permission problem
RUN useradd aria2 && \
	usermod -G aria2 www-data && \
	usermod -G www-data aria2

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
