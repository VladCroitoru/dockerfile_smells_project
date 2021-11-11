FROM jsurf/rpi-raspbian:latest
MAINTAINER Wouter De Schuyter <wouter.de.schuyter@gmail.com>

# PHP version
ENV PHP_VERSION 7.1.5

# Other env variables
ENV PHP_INI_DIR /usr/local/etc/php
ENV PHP_SRC_URL https://secure.php.net/get/php-$PHP_VERSION.tar.xz/from/this/mirror
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=www-data --with-fpm-group=www-data
ENV PHPIZE_DEPS \
		autoconf \
		file \
		g++ \
		gcc \
		libc-dev \
		make \
		pkg-config \
		re2c

# Copy over helper binaries
COPY docker-php-* /usr/local/bin/

# Enable cross build
RUN ["cross-build-start"]

# Install deps
RUN apt-get update \
	&& apt-get install --no-install-recommends -y \
		$PHPIZE_DEPS \
		ca-certificates \
		curl \
		libedit2 \
		libsqlite3-0 \
		libxml2 \
		xz-utils \
	&& apt-get clean \
	&& rm -r /var/lib/apt/lists/*

# Create PHP ini dir
RUN mkdir -p $PHP_INI_DIR/conf.d

# Preparation, download src etc
RUN apt-get update \
	&& apt-get install -y --no-install-recommends wget \
	&& apt-get clean \
	&& rm -r /var/lib/apt/lists/* \
	&& mkdir -p /usr/src \
	&& cd /usr/src \
	&& wget --show-progress -O php.tar.xz $PHP_SRC_URL \
	&& apt-get purge -y --auto-remove wget

# Build
RUN set -xe; \
	buildDeps=" \
		$PHP_EXTRA_BUILD_DEPS \
		libcurl4-openssl-dev \
		libedit-dev \
		libsqlite3-dev \
		libssl-dev \
		libxml2-dev \
	" \
	&& apt-get update \
	&& apt-get install --no-install-recommends -y $buildDeps \
	&& apt-get clean \
	&& rm -r /var/lib/apt/lists/* \
	&& docker-php-source extract \
	&& cd /usr/src/php \
	&& ./configure \
		--with-config-file-path="$PHP_INI_DIR" \
		--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \
		--disable-cgi \
		--enable-ftp \
		--enable-mbstring \
		--enable-mysqlnd \
		--with-curl \
		--with-libedit \
		--with-openssl \
		--with-zlib \
		\
		$PHP_EXTRA_CONFIGURE_ARGS \
	&& make -j "$(nproc)" \
	&& make install \
	&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-all '{}' + || true; } \
	&& make clean \
	&& docker-php-source delete \
	&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $buildDeps \
	&& apt-get clean \
	&& rm -r /var/lib/apt/lists/*

# Configure
RUN set -ex; \
	cd /usr/local/etc \
	&& { \
		# for some reason, upstream's php-fpm.conf.default has "include=NONE/etc/php-fpm.d/*.conf"
		sed 's!=NONE/!=!g' php-fpm.conf.default | tee php-fpm.conf > /dev/null; \
		cp php-fpm.d/www.conf.default php-fpm.d/www.conf; \
	} \
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

# Disable cross build
RUN ["cross-build-end"]

ENTRYPOINT ["docker-php-entrypoint"]
EXPOSE 9000
CMD ["php-fpm"]
