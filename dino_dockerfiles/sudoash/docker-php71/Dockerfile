FROM php:7.1.0-fpm

RUN echo "deb http://http.us.debian.org/debian/ testing non-free contrib main" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y \
	git \
	vim \
	telnet \
	bzip2 \
	libbz2-dev \
	libfreetype6-dev \
	libjpeg62-turbo-dev \
	libmcrypt-dev \
	libpng12-dev \
	libghc-postgresql-libpq-dev \
	php-pear \
	libpq-dev \
	libmemcached-dev \
	libxml2-dev \
	nodejs nodejs-legacy \
	libxslt1-dev \
	g++ zlib1g-dev libicu-dev \
	&& docker-php-ext-install mcrypt mbstring bz2 bcmath zip \
	&& docker-php-ext-configure gd  -with-freetype-dir=/usr/include/ -with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-configure pgsql -with-pgsql=/usr/include/postgresql/ \
	&& docker-php-ext-install gd pgsql pdo_pgsql pdo_mysql soap intl xsl \
	&& docker-php-ext-enable opcache

RUN pecl install -o -f xdebug \
    && rm -rf /tmp/pear \
    && echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/xdebug.so" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on"  >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_host=10.0.2.2" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_connect_back=On" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.idekey=PHPSTORM" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "memory_limit = 128M" > /usr/local/etc/php/conf.d/php.ini

# Install ImageMagick
RUN runtimeRequirements="libmagickwand-6.q16-dev --no-install-recommends" \
    && apt-get update && apt-get install -y ${runtimeRequirements} \
    && ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config /usr/bin/ \
    && pecl install imagick-3.4.3RC1 \
    && echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \
    && rm -rf /var/lib/apt/lists/*

# Install Memcached
RUN curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-dev/php-memcached/archive/php7.tar.gz" \
    && mkdir -p memcached \
    && tar -C memcached -zxvf /tmp/memcached.tar.gz --strip 1 \
    && ( \
        cd memcached \
        && phpize \
        && ./configure \
        && make -j$(nproc) \
        && make install \
    ) \
    && rm -r memcached \
    && rm /tmp/memcached.tar.gz \
    && docker-php-ext-enable memcached


# Install Redis
RUN mkdir -p /usr/src/php/ext/ \
    && curl -L -o /tmp/redis.tar.gz https://github.com/phpredis/phpredis/archive/3.0.0.tar.gz \
    && tar xfz /tmp/redis.tar.gz \
    && rm -r /tmp/redis.tar.gz \
    && mv phpredis-3.0.0 /usr/src/php/ext/redis \
    && docker-php-ext-install redis

# Install npm, bower and gulp
RUN curl -L https://npmjs.org/install.sh | sh \
    && npm install bower -g \
    && npm install gulp -g \

    # The "v" query parameter forces docker to rebuild this build layer, i.e. it's not something
    # composer.org interprets. In practice, the latest composer version is always installed.
    && curl -sS "https://getcomposer.org/installer?v=1.3.1" | php \
    && mv composer.phar /usr/bin/composer \

    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["php-fpm", "-F"]

EXPOSE 9000
