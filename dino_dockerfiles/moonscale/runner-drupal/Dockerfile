FROM php:7.2-apache

ENV DEBCONF_FRONTEND non-interactive
ENV PHPREDIS_VERSION 3.1.4

ADD bin/docker-php-pecl-install /usr/local/bin/

RUN apt-get update && apt-get install -y \
        git \
        imagemagick \
        libapache2-mod-rpaf \
        libcurl4-openssl-dev \
        libfreetype6-dev \
        libjpeg-turbo-progs \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libmemcached-dev \
        libpng-dev \
        libxml2-dev \
        mysql-client \
        pngquant \
        redis-tools \
        ssmtp \
        sudo \
        unzip \
        wget \
        zlib1g-dev \
    && mkdir -p /usr/src/php/ext/redis \
	   && curl -L https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz | tar xvz -C /usr/src/php/ext/redis --strip 1 \
	   && echo 'redis' >> /usr/src/php-available-exts \
    && docker-php-ext-install \
        bcmath \
        curl \
        exif \
        mbstring \
        mysqli \
        opcache \
        pcntl \
        pdo_mysql \
        redis \
        soap \
        zip \
    && apt-get clean && apt-get autoremove -q \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man /tmp/* \
    && a2enmod deflate expires headers mime rewrite \
    && echo "<Directory /var/www/html>\nAllowOverride All\n</Directory>" > /etc/apache2/conf-enabled/allowoverride.conf \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && git clone https://github.com/php-memcached-dev/php-memcached /usr/src/php/ext/memcached \
    && cd /usr/src/php/ext/memcached && git checkout 6ace07da69a5ebc021e56a9d2f52cdc8897b4f23 \
    && docker-php-ext-configure memcached \
    && docker-php-ext-install memcached \
    && echo "sendmail_path = /usr/sbin/ssmtp -t" > /usr/local/etc/php/conf.d/conf-sendmail.ini \
    && echo "date.timezone='Europe/Paris'\n" > /usr/local/etc/php/conf.d/conf-date.ini

RUN cd /usr/local \
    && curl -sS https://getcomposer.org/installer | php \
    && chmod +x /usr/local/composer.phar \
    && ln -s /usr/local/composer.phar /usr/local/bin/composer

RUN cd /usr/local \
    && git clone http://github.com/drush-ops/drush.git --branch 8.x \
    && cd /usr/local/drush \
    && composer install \
    && ln -s /usr/local/drush/drush /usr/bin/drush
