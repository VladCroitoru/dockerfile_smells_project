FROM php:7.4-apache-buster

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
		libjpeg62-turbo-dev \
		libjpeg-dev \
		libpng-dev \
		libwebp-dev \
		libxpm-dev \
		libpq-dev \
		libzip-dev \
	; \
	\
	docker-php-ext-configure gd \
		--with-freetype \
		--with-jpeg=/usr \
		--with-webp=/usr \
		--with-xpm=/usr \
	; \
	\
	docker-php-ext-install -j "$(nproc)" \
		gd \
		opcache \
		pdo_mysql \
		pdo_pgsql \
		zip \
		bcmath \
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


# Install Memcached for php 7
RUN apt-get update && apt-get install -y libmemcached-dev zlib1g-dev \
		&& pecl install memcached \
		&& docker-php-ext-enable memcached

# Install openssh && nano && supervisor && drush && git
RUN apt-get update && apt-get install -y openssh-server nano supervisor git && php -r "readfile('https://github.com/drush-ops/drush/releases/download/8.4.8/drush.phar');" > drush \
    && php drush core-status \
		&& chmod +x drush \
		&& mv drush /usr/local/bin \
		&& drush init -y

# Install mysql-clients && rsync. In order to sync database with the container
RUN apt-get install -y rsync default-mysql-client

# Install Composer In order to use compose
COPY --from=composer:2 /usr/bin/composer /usr/local/bin/

# ADD Configuration to the Container
ADD conf/supervisord.conf /etc/supervisord.conf
ADD conf/apache2.conf /etc/apache2/apache2.conf
ADD conf/php.ini /usr/local/etc/php/

# Add Scripts
ADD scripts/start.sh /start.sh
RUN chmod 755 /start.sh


EXPOSE 443 80

CMD ["/start.sh"]
