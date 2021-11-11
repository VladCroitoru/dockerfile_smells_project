FROM php:7
MAINTAINER Kosta Harlan <kosta@savaslabs.com>

RUN apt-get update && apt-get install -y libpspell-dev aspell-en git zip \
    && docker-php-ext-install -j$(nproc) pspell

RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

COPY . /usr/src/sumac
WORKDIR /usr/src/sumac

RUN composer install -n --prefer-dist --working-dir=/usr/src/sumac

COPY "config/memory-limit.ini" "$PHP_INI_DIR/conf.d/"

ENTRYPOINT ["php", "sumac.php"]
