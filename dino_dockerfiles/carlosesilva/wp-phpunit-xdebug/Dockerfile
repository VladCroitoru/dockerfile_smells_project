FROM php:7.1-fpm-alpine

# install dependencies needed
RUN apk add --no-cache \
    bash \
    sed \
    git \
    subversion \
    mysql-client

# install the PHP extensions we need
RUN set -ex; \
	apk add --no-cache --virtual .build-deps \
		libjpeg-turbo-dev \
		libpng-dev; \
	docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
	docker-php-ext-install gd mysqli opcache; \
	\
	runDeps="$( \
		scanelf --needed --nobanner --format '%n#p' --recursive /usr/local/lib/php/extensions \
			| tr ',' '\n' \
			| sort -u \
			| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
	)"; \
	apk add --virtual .wordpress-phpexts-rundeps $runDeps; \
	apk del .build-deps

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=2'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

WORKDIR /tmp
# Install phpunit
RUN set -ex; \
    docker-php-ext-install pcntl; \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"; \
    php composer-setup.php --install-dir=/usr/bin --filename=composer; \
    php -r "unlink('composer-setup.php');"; \
    composer require "phpunit/phpunit:~5.7" --prefer-source --no-interaction; \
    composer require "phpunit/php-invoker" --prefer-source --no-interaction; \
    ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit; \
    sed -i 's/nn and/nn, Julien Breux (Docker) and/g' /tmp/vendor/phpunit/phpunit/src/Runner/Version.php

# Install xdebug
RUN set -ex; \
    apk add --no-cache --virtual .build-deps \
      g++ \
      make \
      autoconf; \
    pecl install xdebug; \
    docker-php-ext-enable xdebug; \
    apk del .build-deps; \
    rm -rf /tmp/pear
# Configure xdebug
RUN { \
      echo ''; \
      echo 'xdebug.remote_enable=1'; \
      echo 'xdebug.remote_autostart=1'; \
      echo 'xdebug.remote_host="docker.for.mac.localhost"'; \
      echo 'xdebug.remote_port="9000"'; \
      echo 'xdebug.remote_log="/var/log/xdebug.log"'; \
    } >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

WORKDIR /var/www/html
