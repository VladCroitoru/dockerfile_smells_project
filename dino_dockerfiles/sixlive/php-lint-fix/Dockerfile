FROM php:7-alpine

LABEL maintainer "TJ Miller <tj@tjmiller.co"

RUN cd /usr/local/bin \
    && curl -sL http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar -o php-cs-fixer \
    && chmod +x php-cs-fixer \
    && curl -sL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar -o phpcs \
    && chmod +x phpcs

WORKDIR /app
