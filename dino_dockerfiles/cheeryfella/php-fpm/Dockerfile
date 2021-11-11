FROM alpine:3.4

MAINTAINER CheeryFella <cheeryfella@gmail.com>

ENV PHP_INI_DIR=/usr/local/etc/php \
	GPG_KEYS=1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763 \
	PHP_VERSION=7.0.10 \
	PHP_FILENAME=php-7.0.10.tar.xz \
	PHP_SHA256=348476ff7ba8d95a1e28e1059430c10470c5f8110f6d9133d30153dda4cdf56a

COPY docker-php-ext-* /usr/local/bin/

RUN set -x \
	# phpize deps
	&& apk add --no-cache --virtual .phpize-deps \
		autoconf \
		file \
		g++ \
		gcc \
		git \
		libc-dev \
		make \
		pkgconf \
		re2c \
	# persistent / runtime deps
	&& apk add --no-cache --virtual .persistent-deps \
		ca-certificates \
		curl \
	#
	# ensure www-data user exists
	&& addgroup -g 82 -S www-data \
	&& adduser -u 82 -D -S -G www-data www-data \
	# 82 is the standard uid/gid for "www-data" in Alpine
	# http://git.alpinelinux.org/cgit/aports/tree/main/apache2/apache2.pre-install?h=v3.3.2
	# http://git.alpinelinux.org/cgit/aports/tree/main/lighttpd/lighttpd.pre-install?h=v3.3.2
	# http://git.alpinelinux.org/cgit/aports/tree/main/nginx-initscripts/nginx-initscripts.pre-install?h=v3.3.2
	#
	&& mkdir -p $PHP_INI_DIR/conf.d \
	&& apk add --no-cache --virtual .build-deps \
		curl-dev \
		gnupg \
		libedit-dev \
		libxml2-dev \
		libxslt-dev \
		openssl-dev \
		postgresql-dev \
		sqlite-dev \
	&& curl -fSL "http://php.net/get/$PHP_FILENAME/from/this/mirror" -o "$PHP_FILENAME" \
	&& echo "$PHP_SHA256 *$PHP_FILENAME" | sha256sum -c - \
	&& curl -fSL "http://php.net/get/$PHP_FILENAME.asc/from/this/mirror" -o "$PHP_FILENAME.asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& for key in $GPG_KEYS; do \
		gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	done \
	&& gpg --batch --verify "$PHP_FILENAME.asc" "$PHP_FILENAME" \
	&& rm -r "$GNUPGHOME" "$PHP_FILENAME.asc" \
	&& mkdir -p /usr/src \
	&& tar -Jxf "$PHP_FILENAME" -C /usr/src \
	&& mv "/usr/src/php-$PHP_VERSION" /usr/src/php \
	&& rm "$PHP_FILENAME" \
	&& cd /usr/src/php \
	&& ./configure \
		--with-config-file-path="$PHP_INI_DIR" \
		--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \
		--enable-fpm \
		--with-fpm-user=www-data \
		--with-fpm-group=www-data \
		--with-pdo-pgsql \
		--disable-cgi \
		# --enable-mysqlnd is included here because it's harder to compile after the fact than extensions are (since it's a plugin for several extensions, not an extension in itself)
		--enable-mysqlnd \
		# --enable-mbstring is included here because otherwise there's no way to get pecl to use it properly (see https://github.com/docker-library/php/issues/195)
		--enable-mbstring \
		--with-curl \
		--with-libedit \
		--with-openssl \
		--with-zlib \
		--with-xsl \
	&& make -j"$(getconf _NPROCESSORS_ONLN)" \
	&& make install \
	&& { find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip --strip-all '{}' + || true; } \
	&& make clean \
	&& runDeps="$( \
		scanelf --needed --nobanner --recursive /usr/local \
			| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
			| sort -u \
			| xargs -r apk info --installed \
			| sort -u \
	)" \
	&& apk add --virtual .php-rundeps $runDeps \
	&& apk del .phpize-deps .build-deps \
	&& rm -rf /var/cache/apk/* \
	&& cd /usr/local/etc \
	&& if [ -d php-fpm.d ]; then \
		# for some reason, upstream's php-fpm.conf.default has "include=NONE/etc/php-fpm.d/*.conf"
		sed 's!=NONE/!=!g' php-fpm.conf.default | tee php-fpm.conf > /dev/null; \
		cp php-fpm.d/www.conf.default php-fpm.d/www.conf; \
	else \
		# PHP 5.x don't use "include=" by default, so we'll create our own simple config that mimics PHP 7+ for consistency
		mkdir php-fpm.d; \
		cp php-fpm.conf.default php-fpm.d/www.conf; \
		{ \
			echo '[global]'; \
			echo 'include=etc/php-fpm.d/*.conf'; \
		} | tee php-fpm.conf; \
	fi \
	&& { \
		echo '[global]'; \
		echo 'error_log = /proc/self/fd/2'; \
		echo; \
		echo '[www]'; \
		echo '; if we send this to /proc/self/fd/1, it never appears'; \
		echo 'access.log = /proc/self/fd/2'; \
		echo; \
		echo 'clear_env = no'; \
		echo; \
		echo '; Ensure worker stdout and stderr are sent to the main error log.'; \
		echo 'catch_workers_output = yes'; \
	} | tee php-fpm.d/docker.conf \
	&& { \
		echo '[global]'; \
		echo 'daemonize = no'; \
		echo; \
		echo '[www]'; \
		echo 'listen = [::]:9000'; \
	} | tee php-fpm.d/zz-docker.conf

COPY ./php.ini /usr/local/etc/php/php.ini

WORKDIR /var/www/html

EXPOSE 9000
