# https://www.xoops.org/
FROM php:7.2-apache

# install the PHP extensions we need
RUN set -ex; \
	\
	if command -v a2enmod; then \
		a2enmod rewrite; \
	fi; \
	\
	savedAptMark="$(apt-mark showmanual)"; \
	\
	apt-get update; \
	apt-get install -y --no-install-recommends \
		libjpeg-dev \
		libpng-dev \
		libpq-dev \
	; \
	\
	docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
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
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

WORKDIR /var/www/html

# https://github.com/XOOPS/XoopsCore25/releases
ENV XOOPS_VERSION 2.5.9
# ENV XOOPS_MD5 981177d250839fdf325001c12b4e20ba

RUN apt-get update \
    && apt-get install -y wget unzip libpng-dev libjpeg-progs libvpx-dev \
    && docker-php-ext-install mysqli gd exif \
    && apt-get clean all \
    && wget "https://github.com/XOOPS/XoopsCore25/archive/v${XOOPS_VERSION}.zip" -O xoops.zip \
    && unzip xoops.zip \
    && mv XoopsCore25-2.5.9/htdocs/* . \
    && rm -rf XoopsCore25-2.5.9 \
    && chown -R www-data:www-data . \
    && chmod -R 777 /var/www/html/uploads \
    && chmod -R 777 /var/www/html/include/license.php \
    && mv /var/www/html/xoops_lib /var/www/ \
    && mv /var/www/html/xoops_data /var/www/ \
    && chmod -R 777 /var/www/xoops_lib/modules/protector/configs \
    && chmod -R 777 /var/www/xoops_data/caches \
    && chmod -R 777 /var/www/xoops_data/caches/xoops_cache \
    && chmod -R 777 /var/www/xoops_data/caches/smarty_cache \
    && chmod -R 777 /var/www/xoops_data/caches/smarty_compile \
    && chmod -R 777 /var/www/xoops_data/configs \
    && chmod -R 777 /var/www/xoops_data/data

EXPOSE 80 443
CMD ["apache2-foreground"]
