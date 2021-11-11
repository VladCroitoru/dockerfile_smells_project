FROM php:alpine

RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \
    && echo "date.timezone=${PHP_TIMEZONE:-UTC}" > "$PHP_INI_DIR/conf.d/date_timezone.ini"
RUN apk --no-cache add curl git subversion openssh openssl mercurial tini bash zip

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENV COMPOSER_ALLOW_SUPERUSER 1
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && composer --ansi --version --no-interaction

WORKDIR /app

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["composer"]