FROM php:7.2-fpm-alpine

ENV PHALCON_VERSION=3.4.2
ENV COMPOSER_ALLOW_SUPERUSER=1

RUN NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
	&& apk add --no-cache --virtual .build-deps $PHPIZE_DEPS \
	&& apk add --no-cache --virtual .ext-deps \
		bash \
		gettext-dev \
		zlib-dev \
	&& docker-php-ext-install -j${NPROC} \
		gettext \
		json \
		opcache \
		zip \
	&& pecl install \
                mongodb \
                xdebug \
	&& docker-php-ext-enable mongodb xdebug \
	&& curl -sSL "https://codeload.github.com/phalcon/cphalcon/tar.gz/v${PHALCON_VERSION}" | tar -xz \
    && cd cphalcon-${PHALCON_VERSION}/build \
    && ./install \
    && cp ../tests/_ci/phalcon.ini $(php-config --configure-options | grep -o "with-config-file-scan-dir=\([^ ]*\)" | awk -F'=' '{print $2}') \
    && cd ../../ \
    && rm -r cphalcon-${PHALCON_VERSION} \
    && apk del .build-deps

COPY --from=composer:2 /usr/bin/composer /usr/bin/composer
