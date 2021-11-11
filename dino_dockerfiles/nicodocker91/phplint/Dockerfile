FROM php:7.2-fpm-alpine

MAINTAINER "Nicolas Giraud" <nicolas.giraud.dev@gmail.com>

COPY helper/php-lint.sh /usr/local/bin/phplint
RUN chmod +x /usr/local/bin/phplint \
    && rm -rf /var/cache/apk/* /var/tmp/* /tmp/*

VOLUME ["/data"]
WORKDIR /data/www

ENTRYPOINT ["phplint"]
CMD ["--help"]
