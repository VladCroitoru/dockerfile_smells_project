FROM alpine:latest
RUN set -x \
    && addgroup -g 82 -S www-data \
    && adduser -u 82 -D -S -G www-data www-data
ENV COMPOSER_ALLOW_SUPERUSER=1
ENTRYPOINT [ "/sbin/tini", "-v", "--" ]
CMD [ "/usr/sbin/php-fpm7", "-F", "-O", "-R" ]
COPY --from=composer /usr/bin/composer /usr/bin/composer
RUN apk add --no-cache \
    tini \ 
    php7 \ 
    php7-apcu \ 
    php7-ctype \ 
    php7-curl \ 
    php7-dom \ 
    php7-exif \ 
    php7-fileinfo \ 
    php7-fpm \ 
    php7-gd \ 
    php7-iconv \ 
    php7-intl \ 
    php7-json \ 
    php7-mbstring \ 
    php7-opcache \ 
    php7-pcntl \ 
    php7-phar \ 
    php7-pdo_mysql \ 
    php7-posix \ 
    php7-redis \ 
    php7-session \ 
    php7-simplexml \ 
    php7-sockets \ 
    php7-tokenizer \ 
    php7-xml \ 
    php7-zip && \
    rm -rf /etc/php7/php-fpm.d/www.conf /etc/php7/php.ini && \
    mkdir -p /tmp/opcache && \
    composer -n global require hirak/prestissimo && \
    composer -n global require jderusse/composer-warmup && \
    composer -n global require tm/tooly-composer-script 
COPY ./config/timezone.ini /etc/php7/conf.d/timezone.ini
COPY ./config/opcache-prod.ini /etc/php7/conf.d/opcache.ini
COPY ./config/php-fpm-pool.conf /etc/php7/php-fpm.d/www.conf
COPY ./config/php.ini /etc/php7/php.ini
COPY ./config/php-cli.ini /etc/php7/php-cli.ini
COPY ./config/composer_config.json /root/.composer/config.json
COPY --chown=www-data ./config/composer_config.json /home/www-data/.composer/config.json