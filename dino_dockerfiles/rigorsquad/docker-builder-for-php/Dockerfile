FROM php:cli-alpine

COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/local/bin/

RUN install-php-extensions ctype curl dom filter hash intl json libxml mbstring openssl pdo phar simplexml sodium tokenizer xml xmlwriter zip @composer

RUN apk add nodejs-current yarn
