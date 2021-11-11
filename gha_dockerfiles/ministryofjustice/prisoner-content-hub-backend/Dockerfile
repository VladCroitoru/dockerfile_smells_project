###########################################################################################
# Copy Dockerhub Drupal image
# https://github.com/docker-library/drupal/blob/master/8.9/php7.4/apache-buster/Dockerfile
#
# We copy over the first part of the Drupal dockerhub image.  We don't want the steps
# that come after this (e.g. composer create-project).
###########################################################################################
FROM php:7.4-apache-buster AS base

# install the PHP extensions we need
RUN set -eux; \
	\
	if command -v a2enmod; then \
		a2enmod rewrite; \
	fi; \
	\
	savedAptMark="$(apt-mark showmanual)"; \
	\
	apt-get update; \
	apt-get install -y --no-install-recommends \
		libfreetype6-dev \
		libjpeg-dev \
		libpng-dev \
		libpq-dev \
		libzip-dev \
	; \
	\
	docker-php-ext-configure gd \
		--with-freetype \
		--with-jpeg=/usr \
	; \
	\
	docker-php-ext-install -j "$(nproc)" \
		gd \
		opcache \
		pdo_mysql \
		pdo_pgsql \
		zip \
	; \
	\
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all build dependencies
	apt-mark auto '.*' > /dev/null; \
	apt-mark manual $savedAptMark; \
	ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \
		| awk '/=>/ { print $3 }' \
		| sort -u \
		| xargs -r dpkg-query -S \
		| cut -d: -f1 \
		| sort -u \
		| xargs -rt apt-mark manual; \
	\
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini
###########################################################################################
# Finish copy Dockerhub Drupal image
###########################################################################################
###########################################################################################
# Custom build steps
###########################################################################################
RUN apt-get update && apt-get install -y \
  curl \
  git-core \
  mediainfo \
  unzip \
  && rm -rf /var/lib/apt/lists/*

RUN pecl install uploadprogress \
    && docker-php-ext-enable uploadprogress

RUN pecl install redis \
  && docker-php-ext-enable redis

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
  && php composer-setup.php --install-dir=/bin --filename=composer --version=2.1.8 \
  && php -r "unlink('composer-setup.php');"

# Add the composer bin directory to the path.
ENV PATH="/var/www/html/vendor/bin:${PATH}"

# Set Timezone
RUN echo "date.timezone = Europe/London" > /usr/local/etc/php/conf.d/timezone_set.ini
# Set no memory limit (for PHP running as cli only).
RUN echo 'memory_limit = -1' >> /usr/local/etc/php/php-cli.ini

###########################################################################################
# Copy repository files
###########################################################################################
WORKDIR /var/www/html

# Copy in Composer configuration
COPY composer.json composer.lock ./
# Copy in patches we want to apply to modules in Drupal using Composer
COPY patches/ patches/

# Copy Project
COPY docroot/modules/custom docroot/modules/custom
COPY docroot/themes/custom docroot/themes/custom
COPY docroot/profiles docroot/profiles
COPY ./apache/ /etc/apache2/
COPY docroot/sites/ docroot/sites/
COPY config/ config/

# Remove write permissions for added security
RUN chmod u-w docroot/sites/default/settings.php \
  && chmod u-w docroot/sites/default/services.yml

###########################################################################################
# Create test image
###########################################################################################
FROM base AS test

# Install mysql cli client, required for running certain drush commands.
RUN apt-get update && apt-get install -y \
  mariadb-client

COPY Makefile Makefile
COPY phpunit.xml phpunit.xml

# Remove the memory limit for the CLI only.
RUN echo 'memory_limit = -1' > /usr/local/etc/php/php-cli.ini

# Install dependencies (with dev)
RUN composer install \
  --no-ansi \
  --dev \
  --no-interaction \
  --prefer-dist

# Change ownership of files
RUN chown -R www-data:www-data /var/www

USER www-data
RUN mkdir -p ~/phpunit/browser_output

FROM test as local
USER root
RUN pecl install xdebug-3.0.4 \
  && docker-php-ext-enable xdebug
USER www-data

###########################################################################################
# Create optimised build
#
# This stage should be used in production.
# It has been purposely set as the last stage of this file, so that it becomes the default
# when no build stage has been specified.
###########################################################################################
FROM base as optimised-build

# Install dependencies
RUN composer install \
  --no-ansi \
  --no-dev \
  --optimize-autoloader \
  --no-interaction \
  --prefer-dist

# Change ownership of files
RUN chown -R www-data:www-data ./
RUN chown -R www-data:www-data /var/www

USER www-data
