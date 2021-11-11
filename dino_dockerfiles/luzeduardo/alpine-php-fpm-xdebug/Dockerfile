FROM luzeduardo/alpine-php-fpm
MAINTAINER Eduardo Luz <luz.eduardo@gmail.com>

ENV XDEBUG_VERSION 2.3.3

RUN apk update && apk add --no-cache --virtual .build-deps autoconf gcc make \
    g++ zlib-dev file g++ libc-dev make pkgconf \
    tar curl php-pear tzdata php-dev php-phar libmemcached-dev \
    && apk add php php-cli php-curl php-gd git php-json libmemcached \
    && cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
    && echo "${TIMEZONE}" > /etc/timezone \

#Xdebug
&& cd /tmp && wget http://xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz \
    && tar -zxvf xdebug-$XDEBUG_VERSION.tgz \
    && cd xdebug-$XDEBUG_VERSION && phpize \
    && ./configure --enable-xdebug && make && make install \
    && echo "zend_extension=$(find /usr/lib/php/modules/ -name xdebug.so)" > /etc/php/php.ini \
    && echo "xdebug.remote_enable=on" >> /etc/php/php.ini \
    && echo "xdebug.remote_handler=dbgp" >> /etc/php/php.ini \
    && echo "xdebug.remote_connect_back=1" >> /etc/php/php.ini \
    && echo "xdebug.remote_autostart=on" >> /etc/php/php.ini \
    && echo "xdebug.remote_port=9004" >> /etc/php/php.ini \

#Cleanup
&& rm -rf /tmp/* \
   && rm -rf /var/cache/apk/* \
   && apk del .build-deps && rm -rf tmp/*

# Set Workdir
WORKDIR /var/www/html

# Expose ports
EXPOSE 9000
EXPOSE 9004
# Entry point
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
