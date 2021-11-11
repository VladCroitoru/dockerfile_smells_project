FROM php:7.3-fpm
MAINTAINER  Robin Appelman <robin@icewind.nl>

RUN DEBIAN_FRONTEND=noninteractive ;\
	apt-get update && \
	apt-get install --assume-yes \
		bzip2 \
		nginx \
		libaio-dev \
		wget \
		unzip \
	&& rm -rf /var/lib/apt/lists/*

# php exceptions
RUN apt-get update \
	&& apt-get install -y \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmcrypt-dev \
		libpng-dev \
		libpq5 \
		libpq-dev \
		libsqlite3-dev \
		libcurl4-openssl-dev \
		libicu-dev \
		libzip-dev \
		libmagickwand-dev \
		libmagickcore-dev \
        libonig-dev \
        libldap2-dev \
    && docker-php-ext-configure gd \
        --with-gd \
        --with-jpeg-dir \
        --with-png-dir \
        --with-zlib-dir \
        --with-freetype-dir \
	&& docker-php-ext-install iconv zip pdo pdo_pgsql pdo_sqlite pgsql pdo_mysql intl curl mbstring gd pcntl ldap \
	&& pecl install imagick \
    && pecl install inotify \
	&& apt-get remove -y \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmcrypt-dev \
		libpng-dev \
		libpq-dev \
		libsqlite3-dev \
		libcurl4-openssl-dev \
		libicu-dev \
		libzip-dev \
		libmagick-dev \
		libmagickwand-dev \
		libmagickcore-dev \
        libonig-dev \
        libldap2-dev \
	&& rm -rf /var/lib/apt/lists/* 

RUN pecl install apcu \
	&& pecl install xdebug \
	&& pecl install redis \
	&& export VERSION=`php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;"` \
    && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s https://blackfire.io/api/v1/releases/probe/php/linux/amd64/${VERSION} \
    && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \
    && mv /tmp/blackfire-*.so `php -r "echo ini_get('extension_dir');"`/blackfire.so \
    && echo "extension=imagick.so" > $PHP_INI_DIR/conf.d/imagick.ini \
    && echo "extension=inotify.so" > $PHP_INI_DIR/conf.d/inotify.ini \
    && echo "extension=blackfire.so\nblackfire.agent_socket=\${BLACKFIRE_PORT}" > $PHP_INI_DIR/conf.d/blackfire.ini \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > $PHP_INI_DIR/conf.d/xdebug.ini \
    && echo "xdebug.mode=debug,trace,profile" >> $PHP_INI_DIR/conf.d/xdebug.ini \
    && echo "xdebug.start_with_request=trigger" >> $PHP_INI_DIR/conf.d/xdebug.ini \
    && echo "xdebug.remote_port=9000" >> $PHP_INI_DIR/conf.d/xdebug.ini \
    && echo "xdebug.discover_client_host=true" >> $PHP_INI_DIR/conf.d/xdebug.ini \
    && echo "memory_limit = 512M" > $PHP_INI_DIR/conf.d/memory_limit.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
    
ADD apcu.ini opcache.ini redis.ini $PHP_INI_DIR/conf.d/

ADD nginx.conf nginx-app.conf /etc/nginx/


ADD php-fpm.conf /usr/local/etc/
ADD index.php /var/www/html/

ADD bootstrap-nginx.sh /usr/local/bin/

EXPOSE 80

ENTRYPOINT  ["bootstrap-nginx.sh"]
