#FROM alpine
FROM kissjared/docker-alpine-base

MAINTAINER weiboyi lijie1@weiboyi.com

ENV APP_ROOT="/opt" \
    XDEBUG_URL="https://xdebug.org/files/xdebug-2.5.0.tgz" \
    REDIS_URL="http://pecl.php.net/get/redis-3.1.2.tgz" \
    MQC_URL="https://github.com/alanxz/rabbitmq-c/releases/download/v0.8.0/rabbitmq-c-0.8.0.tar.gz" \
    MQ_URL="http://pecl.php.net/get/amqp-1.9.0.tgz"

RUN PHP_CONFIG="--with-php-config=/usr/bin/php-config5" \
    MQC_PATH="/usr/local/rabbitmq-c-0.8.0" \
    && apk add --update --no-cache \
            wget \
            pcre-dev \
            build-base \
            autoconf \
            libtool \
            openssl \
            openssl-dev \
            supervisor \
            mysql-client \
            nginx \
            php5-fpm \
            php5-mcrypt \
            php5-dev \
            php5-soap \
            php5-openssl \
            php5-gmp \
            php5-pdo_odbc \
            php5-json \
            php5-dom \
            php5-pdo \
            php5-zip \
            php5-mysql \
            php5-mysqli \
            php5-sqlite3 \
            php5-bcmath \
            php5-gd \
            php5-pdo_mysql \
            php5-pdo_sqlite \
            php5-gettext \
            php5-xmlreader \
            php5-xmlrpc \
            php5-bz2 \
            php5-mssql \
            php5-iconv \
            php5-pdo_dblib \
            php5-curl \
            php5-ctype \
            php5-odbc \
            php5-intl \
            php5-opcache \
            php5-phar \
            php5-xml \
            php5-posix  \
    && ln -s /usr/bin/php5 /usr/bin/php \
    && ln -s /usr/bin/phpize5 /usr/bin/phpize \
    # dowload pkg
    && cd /mnt \
    && for URL in \
           $XDEBUG_URL \
           $REDIS_URL \
           $MQC_URL \
           $MQ_URL \
       ; do \
           wget -qO- --no-check-certificate "$URL" | tar xvz -C /mnt/; \
       done \
    # install php-redis
    #&& tar xf redis-3.1.2.tgz \
    && cd redis-3.1.2 \
    && /usr/bin/phpize5 \
    && ./configure $PHP_CONFIG \
    && make \
    && make install \
    # install php-xdebug
    && cd /mnt \
    #&& tar xf xdebug-2.5.0.tgz \
    && cd xdebug-2.5.0 \
    && /usr/bin/phpize5 \
    && ./configure $PHP_CONFIG \
    && make \
    && make install \
    # install php-amqp-rabbitmq-c
    && cd /mnt \
   # && tar xf rabbitmq-c-0.8.0.tar.gz \
    && cd rabbitmq-c-0.8.0 \
    && ./configure --prefix=$MQC_PATH \
    && make \
    && make install \
    # install php-amqp
    && cd /mnt \
    #&& tar xf amqp-1.9.0.tgz \
    && cd amqp-1.9.0 \
    && /usr/bin/phpize5 \
    && ./configure $PHP_CONFIG -with-amqp --with-librabbitmq-dir=$MQC_PATH \
    && make \
    && make install \
    && mkdir /etc/supervisor.d \
    && adduser -D -u 1000 -g 'www' www \
    # Purge dev APK packages
    && apk del --purge \
            *-dev \
            build-base \
            autoconf \
            libtool \
    # Cleanup after phpizing
    && rm -fr /usr/include/php \
    && rm -fr /usr/lib/php/build \
    && rm -fr /usr/lib/php5/modules/*.a \
    # Final cleanup
    && rm -fr /var/cache/apk/* \
    && rm -fr /tmp/* \
    && rm -fr /usr/share/man \
    && rm -fr /mnt/*

WORKDIR ${APP_ROOT}
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY config/nginx/mime.types /etc/nginx/mime.types
COPY config/nginx/conf.d/*   /etc/nginx/conf.d/
COPY config/php/php-fpm.conf /etc/php5/php-fpm.conf
COPY config/php/php.ini /etc/php5/php.ini
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/supervisor.d/* /etc/supervisor.d/
COPY www/* /var/www/
COPY ./startup.sh /opt/
RUN chmod +x /opt/startup.sh && chown www:www /var/www -R

EXPOSE 80

VOLUME ["/var/www"]

CMD ["/opt/startup.sh"]
