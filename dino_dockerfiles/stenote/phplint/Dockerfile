FROM php:alpine

RUN apk add --no-cache git wget unzip

RUN wget https://getcomposer.org/composer.phar && \
    chmod a+x composer.phar && \
    mv composer.phar /usr/local/bin/composer

RUN composer global require overtrue/phplint

ENV PATH $PATH:/root/.composer/vendor/bin
