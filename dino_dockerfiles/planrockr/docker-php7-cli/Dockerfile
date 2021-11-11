FROM eminetto/docker-php7-cli
RUN apt-get update \
    && apt-get install -y software-properties-common git libmemcached-dev zlib1g-dev libicu-dev g++\
    && pecl install mongodb \
    && echo "extension=mongodb.so" >> /usr/local/etc/php/conf.d/mongodb.ini \
    && git clone https://github.com/php-memcached-dev/php-memcached.git \
    && cd php-memcached \
    && git checkout php7 \
    && phpize \
    && ./configure --disable-memcached-sasl \
    && make \
    && make install \
    && echo "extension=memcached.so" >> /usr/local/etc/php/conf.d/memcached.ini \
    && docker-php-ext-install -j$(nproc) bcmath intl \
    && pecl install xdebug \
    && echo "memory_limit = 12800M" >> /usr/local/etc/php/conf.d/666-custom.ini
