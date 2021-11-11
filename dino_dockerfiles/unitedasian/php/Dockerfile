FROM php:7.0

ARG timezone='Asia/Hong_Kong'

ARG memory_limit=-1

RUN apt-get update && apt-get install -y \
        git \
        graphviz \
        libicu-dev \
        libldap2-dev \
        libmcrypt-dev \
        openssh-client \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure ldap --with-libdir=/lib/x86_64-linux-gnu/ \
    && docker-php-ext-install \
        intl \
        ldap\
        mcrypt \
        pdo_mysql \
        zip \
    && echo "date.timezone="$timezone > /usr/local/etc/php/conf.d/date_timezone.ini \
    && echo "memory_limit="$memory_limit > /usr/local/etc/php/conf.d/memory_limit.ini \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
