FROM composer:latest AS composer

# Install the project packages
WORKDIR /tmp
COPY composer.json /tmp/
RUN composer --ansi install

FROM alpine:3.10 AS dist

RUN apk add --no-cache bash curl tini nginx \
    php7-fpm php7-json php7-ctype php7-mbstring php7-curl \
    && mkdir -p /run/nginx \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

# Healthcheck
HEALTHCHECK --timeout=3s \
    CMD curl http://localhost || exit 1

# Environment variables
ENV SENTRY_DSN=https://a115369e208847449cc6c05f4d332672:0ad536e676074277a1a9c2d6dfba6da6@sentry.io/119540

# Install the codebase
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY build/nginx.conf /etc/nginx/nginx.conf
COPY build/php-fpm.conf /etc/php7/php-fpm.d/zz-docker.conf
COPY src /var/www
COPY --from=composer /tmp/vendor /var/www/vendor

WORKDIR /var/www
ENTRYPOINT [ "/sbin/tini" ]
CMD [ "/docker-entrypoint.sh" ]
