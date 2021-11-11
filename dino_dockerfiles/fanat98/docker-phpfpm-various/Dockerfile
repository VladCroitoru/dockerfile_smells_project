FROM php:8.0-fpm
MAINTAINER Aslam Idrisov <aslam@malsa.ch>


# Install general utilities
RUN apt-get update \
	&& apt-get install -y \
		vim \
		net-tools \
		procps \
		telnet \
		libpcre3-dev \
		libonig-dev \
		libxml2-dev \
		netcat \
		libzip-dev \
	&& rm -r /var/lib/apt/lists/*

RUN apt-get update \
	&& apt-get install -y \
		imagemagick \
		graphicsmagick \
		zip \
		unzip \
		wget \
		curl \
		git \
		mariadb-client \
		moreutils \
		dnsutils \
		ffmpeg \
	&& rm -rf /var/lib/apt/lists/*

# gd
RUN buildRequirements="libpng-dev libjpeg-dev libfreetype6-dev" \
	&& apt-get update && apt-get install -y ${buildRequirements} \
	&& docker-php-ext-configure gd --with-freetype=/usr/include/ --with-jpeg=/usr/lib \
	&& docker-php-ext-install gd \
	&& apt-get purge -y ${buildRequirements} \
	&& rm -rf /var/lib/apt/lists/*
	
RUN curl http://ftp.debian.org/debian/pool/main/i/icu/libicu63_63.2-3_amd64.deb \
--output libicu63_63.2-3_amd64.deb && dpkg -i libicu63_63.2-3_amd64.deb

# intl
RUN buildRequirements="libicu-dev g++" \
	&& apt-get update && apt-get install -y ${buildRequirements} \
	&& docker-php-ext-install intl \
	&& apt-get purge -y ${buildRequirements} \
	&& apt-get install -y --auto-remove ${runtimeRequirements} \
	&& rm -rf /var/lib/apt/lists/*


# Install extensions
# ref to: https://github.com/mlocati/docker-php-extension-installer
ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/

RUN chmod +x /usr/local/bin/install-php-extensions && sync && \
	install-php-extensions \
	opcache \
	imagick \
	mysqli \
	mbstring \
	redis \
	pdo_mysql \
	yaml \
	zip \
	&& \
	rm -rf /tmp/* /var/cache/apk/*

# redis
RUN echo "extension=redis.so" > /usr/local/etc/php/conf.d/ext-redis.ini \
	&& rm -rf /tmp/redis.tar.gz /tmp/redis

# APCu
RUN pecl install apcu \
	&& echo "extension=apcu.so\napc.enable_cli = 1" > /usr/local/etc/php/conf.d/ext-apcu.ini

# create symlink to support standard /usr/bin/php
RUN ln -s /usr/local/bin/php /usr/bin/php

# locales
ADD assets/locale.gen /etc/locale.gen
RUN apt-get update \
	&& apt-get install -y locales \
	&& rm -r /var/lib/apt/lists/*

# Activate login for user www-data
RUN chsh www-data -s /bin/bash

# new home folder for user
RUN usermod -d /data/web/releases/current www-data


ADD assets/php-fpm.conf /usr/local/etc/php-fpm.conf
ADD assets/php.ini /usr/local/etc/php/conf.d/php.ini
ADD assets/.env.docker /opt/docker/.env.docker
ADD assets/entrypoint.sh /entrypoint.sh
ADD assets/bin /usr/local/bin

# Cron
RUN apt-get update \
	&& apt-get install -y cron \
	&& rm -rf /var/lib/apt/lists/*


#####################################
# Exif:
#####################################

ARG INSTALL_EXIF=true
RUN if [ ${INSTALL_EXIF} = true ]; then \
	# Enable Exif PHP extentions requirements
	docker-php-ext-install exif && \
	 docker-php-ext-enable exif \
;fi


WORKDIR /data/web/releases/current

ENTRYPOINT ["/entrypoint.sh"]
CMD ["php-fpm"]