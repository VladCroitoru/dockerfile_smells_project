FROM debian:jessie

MAINTAINER "Vitor Carreira" <vitor.carreira@gmail.com>

WORKDIR /tmp

# Common PHP pages across containers
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    php5-cli \
    php5-mcrypt \
    php5-mysqlnd \
    php5-apcu \
    php5-memcached \
    php5-imap \
    php5-pgsql \
    php5-intl \
    php5-redis \
    php5-mongo \
    php5-sqlite \
    php5-curl \
    php5-json \
    php5-ssh2 \
    php5-gd \
    php5-gmp \
    php-pear \
    php5-dev make  \
    wget \
    git \
    curl && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["php", "-a"]
