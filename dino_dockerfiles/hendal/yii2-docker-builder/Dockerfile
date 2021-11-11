FROM php:7.1.9

RUN apt-get update -yqq && apt-get install -yqq git libmcrypt-dev libpq-dev libcurl4-gnutls-dev libicu-dev libvpx-dev \
                libjpeg-dev libpng-dev libxpm-dev zlib1g-dev libfreetype6-dev libxml2-dev libexpat1-dev zip \
                libbz2-dev libgmp3-dev libldap2-dev unixodbc-dev libsqlite3-dev libaspell-dev libsnmp-dev libpcre3-dev libtidy-dev
RUN docker-php-ext-install mbstring mcrypt pdo_pgsql curl json intl gd xml zip bz2 opcache
ENV COMPOSER_CACHE_DIR=/cache/composer
RUN mkdir /build \
 && mkdir /composer \
 && chmod -R 777 /composer \
 && curl -sfLo /tmp/composer-setup.php https://getcomposer.org/installer \
 && curl -sfLo /tmp/composer-setup.sig https://composer.github.io/installer.sig \
 && php -r " \
    \$hash = hash('SHA384', file_get_contents('/tmp/composer-setup.php')); \
    \$signature = trim(file_get_contents('/tmp/composer-setup.sig')); \
    if (!hash_equals(\$signature, \$hash)) { \
        unlink('/tmp/composer-setup.php'); \
        echo 'Integrity check failed, installer is either corrupt or worse.' . PHP_EOL; \
        exit(1); \
    }" \
 && php /tmp/composer-setup.php --no-ansi --install-dir=/usr/bin --filename=composer \
 && composer --no-interaction --no-ansi --version \
 && rm /tmp/composer-setup.php \
 && composer global require "fxp/composer-asset-plugin:^1.2.0"
