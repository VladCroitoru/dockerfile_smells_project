FROM php:7.2-fpm-alpine

MAINTAINER "Nicolas Giraud" <nicolas.giraud.dev@gmail.com>
MAINTAINER "Pierre-Arthur Desportes" <pierre-arthur.desportes@aareon.fr>

RUN curl -Ls https://phar.phpunit.de/phpunit.phar > /usr/local/bin/phpunit && \
    chmod +x /usr/local/bin/phpunit && \
    # Then here we go to install the whole universe for xdebug to enable the code coverage...
    apk update && \
    apk add --no-cache g++ make autoconf zlib-dev && \
    docker-php-source extract && \
    pecl install xdebug && \
    docker-php-ext-install zip && \
    docker-php-ext-enable xdebug && \
    docker-php-source delete && \
    echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \
    echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \
    echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \
    echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \
    echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \

    apk del g++ make autoconf && \

    rm -rf /var/lib/apt/lists/* /var/cache/apk/* /tmp/*

VOLUME ["/data"]
WORKDIR /data/www

ENTRYPOINT ["phpunit"]
CMD ["--help"]
