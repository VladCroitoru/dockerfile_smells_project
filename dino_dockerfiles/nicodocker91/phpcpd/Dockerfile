FROM php:7.2-fpm-alpine

MAINTAINER "Nicolas Giraud" <nicolas.giraud.dev@gmail.com>

RUN curl -Ls https://phar.phpunit.de/phpcpd.phar > /usr/local/bin/phpcpd \
    && chmod +x /usr/local/bin/phpcpd \
    && rm -rf /var/cache/apk/* /var/tmp/* /tmp/*

VOLUME ["/data"]
WORKDIR /data/www

ENTRYPOINT ["phpcpd"]
CMD ["--version"]
