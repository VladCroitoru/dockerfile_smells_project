FROM php:7.4-fpm-alpine

ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-installer/master/install-php-extensions /usr/local/bin/
ADD entrypoint.sh /entrypoint.sh

RUN set -xe \
	&& apk add --no-cache pcre-dev ${PHPIZE_DEPS} \
		libmcrypt-dev \
		libxml2-dev \
		libintl \
		gettext-dev \
		openldap-dev \
		freetype-dev \
		libjpeg-turbo-dev	 \
		libpng-dev \
		icu-dev \
		git \
		bash \
		openssh \

	# Install composer and prestissimo
	&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \

	&& docker-php-ext-configure gd --with-freetype --with-jpeg \

	&& chmod uga+x /usr/local/bin/install-php-extensions \
	&& sync \
    && install-php-extensions bcmath memcached apcu \
        calendar fileinfo iconv json mbstring \
        gettext mcrypt pcntl pdo pdo_mysql soap \
        tokenizer zip ldap gd intl xdebug \

	&& rm -rf /var/cache/apk/* \
	&& apk del pcre-dev ${PHPIZE_DEPS} \
	&& chmod +x /entrypoint.sh

COPY .docker/www.conf /usr/local/etc/php-fpm.d/
COPY .docker/docker-php-memory-limit.ini /usr/local/etc/php/conf.d/
COPY .docker/docker-php-ext-xdebug-disabled.ini /usr/local/etc/php/
COPY .docker/docker-php-ext-xdebug-enabled.ini /usr/local/etc/php/

ENTRYPOINT ["/entrypoint.sh"]
