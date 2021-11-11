FROM php:7.0
MAINTAINER zacksleo <zacks.leo@gmail.com>
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        openssh-client \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libcurl4-openssl-dev \
        libldap2-dev \
        curl \
        libtidy* \
    && rm -r /var/lib/apt/lists/*

# PHP Extensions
RUN docker-php-ext-install \
    mcrypt \
    mbstring \
    curl \
    json \
    pdo_mysql \
    exif \
    tidy \
    zip \
    	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
        && docker-php-ext-install gd \
        && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \
	&& docker-php-ext-install ldap
  
# Memory Limit
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini

# Time Zone
RUN echo "date.timezone=Asia/Chongqing" > $PHP_INI_DIR/conf.d/date_timezone.ini

VOLUME /root/composer

# Environmental Variables
ENV COMPOSER_HOME /root/composer




RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer.phar \
    && composer.phar global require --no-progress "fxp/composer-asset-plugin:~1.2.2" \
    && composer.phar global require --no-progress "codeception/codeception=2.0.*" \
    && composer.phar global require --no-progress "codeception/specify=*" \
    && composer.phar global require --no-progress "codeception/verify=*"
    && composer.phar gloabl require --no-progress "phpunit/phpunit" \
    && composer.phar global require --no-progress "squizlabs/php_codesniffer" \
    && composer.phar gloabl require --no-grogress "phpmd/phpmd" \
    && composer selfupdate

# Goto temporary directory.
WORKDIR /tmp

