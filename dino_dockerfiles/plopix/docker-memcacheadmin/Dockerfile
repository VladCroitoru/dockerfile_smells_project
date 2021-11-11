FROM php:5.6-alpine
MAINTAINER Plopix

RUN apk --update add libtool libmemcached-dev libmemcached libmemcached-libs \
    zlib-dev && echo "yes  --disable-memcached-sasl" | pecl install memcached &&\
    echo "extension=memcached.so" >> /usr/local/etc/php/php.ini

ADD http://phpmemcacheadmin.googlecode.com/files/phpMemcachedAdmin-1.2.2-r262.tar.gz /tmp/admin.tar.gz

RUN mkdir -p /var/www/html/memcachedadmin && tar xvzf /tmp/admin.tar.gz -C /var/www/html/memcachedadmin

ENV MEMCACHE_HOST memcache
ENV MEMCACHE_PORT 11211

COPY config.php /var/www/html/memcachedadmin/Config/Memcache.php

EXPOSE 9083

CMD ["php", "-S", "0.0.0.0:9083", "-t", "/var/www/html/memcachedadmin"]
