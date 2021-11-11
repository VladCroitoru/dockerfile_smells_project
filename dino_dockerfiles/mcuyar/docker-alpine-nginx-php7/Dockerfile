FROM mcuyar/docker-alpine-nginx
MAINTAINER Matthew Cuyar <matt@enctypeapparel.com>

#----------------------------------------------------
# Base Alpine edge image w/s6 Overlay, Nginx and PHP7
#----------------------------------------------------

##/
 # Install PHP
 #/
RUN apk --no-cache --update --repository=http://dl-4.alpinelinux.org/alpine/v3.7/main add \
    # Global Packages
    curl \
    git \
    # PHP Packages
    php7 \
    php7-fpm \
    php7-xml \
    php7-pgsql \
    php7-pdo_pgsql \
    php7-mysqli \
    php7-pdo_mysql \
    php7-mcrypt \
    php7-opcache \
    php7-gd \
    php7-curl \
    php7-json \
    php7-phar \
    php7-openssl \
    php7-ctype \
    php7-mbstring \
    php7-zip \
    php7-dom \
    php7-pcntl \
    php7-posix \
    php7-session \
    php7-zlib \
    php7-tokenizer \
    php7-simplexml \
    php7-xmlwriter \
    php7-fileinfo \
    php7-ftp \
    php7-iconv \
    php7-xmlreader

##/
 # Install composer
 #/
ENV COMPOSER_HOME=/composer
ENV COMPOSER_ALLOW_SUPERUSER=1
ENV PATH $COMPOSER_HOME/vendor/bin:$PATH

RUN mkdir /composer \
    && curl -sS https://getcomposer.org/installer | php \
    && mkdir -p /opt/composer \
    && mv composer.phar /opt/composer/composer.phar

##/
 # Install New Relic PHP Agent
 #/
RUN mkdir /tmp/newrelic \
    && cd /tmp/newrelic \
    && wget "https://download.newrelic.com/php_agent/release/$(curl -s https://download.newrelic.com/php_agent/release/ | grep -ohE 'newrelic-php5-.*?-linux-musl.tar.gz' | cut -f1 -d\")" -O php-agent.tar.gz \
    && gzip -dc php-agent.tar.gz | tar xf - \
    && mkdir -p /opt/newrelic \
    && cp -a "$(ls | grep 'newrelic')/." /opt/newrelic/ \
    && rm -rf /tmp/newrelic

WORKDIR /var/www

##/
 # Copy files
 #/
COPY rootfs /
