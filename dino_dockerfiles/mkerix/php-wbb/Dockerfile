FROM php:7.1-fpm

RUN apt-get update \
    && apt-get install -y default-mysql-client \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install pdo_mysql \
    && sed -i 's/pm.max_children = 5/pm.max_children = 10/g' /usr/local/etc/php-fpm.d/www.conf
