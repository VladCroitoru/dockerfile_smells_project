FROM php:7.0-apache
MAINTAINER Rafael Kutscha <giginos@web.de>

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        ant \
        git \
        unzip \
        mysql-client \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev && \
    docker-php-ext-install -j5 \
        opcache \
        gd \
        mcrypt \
        pdo_mysql \
        zip && \
    rm -rf /var/lib/apt/lists/* && \
    a2enmod rewrite
    
ENV \
    SHOPWARE_VERSION=5.2.3 \
    COMPOSER_VERSION=1.1.2 \
    MYSQL_HOST=db \
    MYSQL_USER=root \
    MYSQL_PASSWORD=root \
    MYSQL_DATABASE=shopware

RUN wget -qO /root/shopware.tar.gz https://github.com/giginos/shopware/archive/v$SHOPWARE_VERSION.tar.gz && \
    wget -qO /usr/local/bin/composer https://getcomposer.org/download/$COMPOSER_VERSION/composer.phar && \
    chmod 755 /usr/local/bin/composer

COPY rootfs/ /
VOLUME /var/www/html

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]