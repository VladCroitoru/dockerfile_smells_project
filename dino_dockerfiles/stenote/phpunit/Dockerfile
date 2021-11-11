FROM php:alpine

RUN apk add --no-cache git wget unzip g++ make autoconf

RUN pecl install xdebug && \
    docker-php-ext-enable xdebug

RUN wget https://getcomposer.org/composer.phar && \
    chmod a+x composer.phar && \
    mv composer.phar /usr/local/bin/composer

RUN composer global require phpunit/phpunit phpunit/php-code-coverage

ENV PATH $PATH:/root/.composer/vendor/bin
