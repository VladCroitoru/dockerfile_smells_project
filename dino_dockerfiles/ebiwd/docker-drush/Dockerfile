FROM ebiwd/alpine-ssh:3.13

LABEL maintainer www-dev@ebi.ac.uk

ARG DRUSHVER=8.1.17

RUN apk add --no-cache \
    curl \
    git \
    mysql-client \
    patch \
    wget \
    zip \
    jq \
    php7 \
    php7-ctype \
    php7-curl \
    php7-dom \
    php7-fileinfo \
    php7-gd \
    php7-json \
    php7-mbstring \
    php7-mcrypt \
    php7-mysqli \
    php7-openssl \
    php7-pcntl \
    php7-pdo_sqlite \
    php7-posix \
    php7-phar \
    php7-session \
    php7-simplexml \
    php7-sqlite3 \
    php7-tokenizer \
    php7-xml \
    php7-xmlwriter \
    php7-zlib

RUN ln -svf /usr/bin/php7 /usr/bin/php
RUN echo 'memory_limit = -1' >> /etc/php7/conf.d/docker-php-memlimit.ini;

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

RUN composer global require drush/drush:${DRUSHVER} \
  && ln -s /root/.composer/vendor/bin/drush /usr/bin/drush

COPY files /

WORKDIR /workspace
