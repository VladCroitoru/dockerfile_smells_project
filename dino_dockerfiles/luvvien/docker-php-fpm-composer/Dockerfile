FROM php:fpm

RUN apt-get update && apt-get install -y locales git curl wget libmagickwand-dev gnupg --no-install-recommends \
    && docker-php-ext-install gd pdo_mysql zip opcache \
    
    && curl -sS https://getcomposer.org/installer | php -d detect_unicode=Off \
    && chmod a+x composer.phar && mv composer.phar /usr/local/bin/composer \
    && composer self-update \

    && curl -sL https://deb.nodesource.com/setup_9.x | bash - \
    && apt-get install -y nodejs --fix-missing \

    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*