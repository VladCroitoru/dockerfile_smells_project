FROM alpine:3.7

ENV FF_VERSION 4.6.8

ENV FF_APP_KEY=SomeRandomStringOf32CharsExactly
ENV FF_APP_ENV=production

COPY entrypoint.sh /

RUN    apk update && apk add --no-cache  \
    php7 \
    php7-fpm \
    php7-openssl \
    php7-mbstring \
    php7-json \
    php7-phar \
    php7-zlib \
    php7-zip \
    php7-bcmath \
    php7-intl \
    php7-curl \
    php7-session \
    php7-ctype \
    php7-pdo_mysql \
    php7-pdo_pgsql \
    php7-tokenizer \
    supervisor \
    gettext \
    curl \
    nginx \
    tzdata && \
   mkdir -p /var/www/localhost/htdocs/firefly /run/nginx && \
   curl -sSL https://github.com/firefly-iii/firefly-iii/archive/${FF_VERSION}.tar.gz | tar xz -C /var/www/localhost/htdocs/firefly --strip-components=1 && \
   cd /var/www/localhost/htdocs/firefly && \
   curl -sSL https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer && \
   composer install --prefer-dist --no-dev --no-scripts && \
   find /var/www/localhost/htdocs/ -type d -exec chmod 770 {} \; && \
   find /var/www/localhost/htdocs/ -type f -exec chmod 660 {} \; && \
   chown -R nginx:nobody /var/www/localhost/htdocs/ && \
   chmod +x /entrypoint.sh
 

RUN ln -s /tmp/test/.env /var/www/localhost/htdocs/firefly/.env  

COPY custom.conf /etc/nginx/conf.d/default.conf
COPY supervisord.conf /tmp/

VOLUME  /tmp/test/

WORKDIR  /var/www/localhost/htdocs/firefly

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]

LABEL url=https://github.com/firefly-iii/firefly-iii/
LABEL version=${FF_VERSION}

CMD ["/usr/bin/supervisord", "-c /tmp/supervisord.conf"]
