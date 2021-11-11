FROM tsari/php
MAINTAINER Tibor Sári <tiborsari@gmx.de>

ENV AMQP_VERSION=1.9.0

# update, install project dependent modules and clean up to minimize the image size
RUN \
    apt-get update -qq && \
    apt-get install --no-install-recommends -y \
        librabbitmq-dev \
        php7.1-apcu \
        php7.1-curl \
        php7.1-dev \
        php7.1-imagick \
        php7.1-intl \
        php7.1-memcached \
        php7.1-mbstring \
        php7.1-sqlite3 \
        php7.1-xml \
        php-zip \
        php-pear \
    && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pecl install amqp-$AMQP_VERSION
RUN echo "extension=`find / -name "amqp.so"`" > /etc/php/7.1/mods-available/amqp.ini && \
    phpenmod amqp

RUN pecl install mongodb
RUN echo "extension=`find / -name "mongodb.so"`" > /etc/php/7.1/mods-available/mongodb.ini && \
    phpenmod mongodb

# this is copied from official php-fpm repo
COPY docker.conf /etc/php/7.1/fpm/pool.d/docker.conf
COPY zz-docker.conf /etc/php/7.1/fpm/pool.d/zz-docker.conf

RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.1/fpm/php.ini

VOLUME /var/www
WORKDIR /var/www

EXPOSE 9000
CMD ["php-fpm7.1"]