FROM php:7.0.11-fpm
MAINTAINER Petter Kjelkenes <kjelkenes@gmail.com>

RUN apt-get update \
  && apt-get install -y \
    git \
    cron \
    libfreetype6-dev \
    libicu-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libxslt1-dev \
    python-pip \
    redis-tools \
    supervisor


# AWS cli is nice to have on aws, think: PaaS.
RUN pip install awscli

# Eb cli is nice to have on aws, think: PaaS.
RUN pip install --upgrade awsebcli

RUN docker-php-ext-configure \
  gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/

RUN docker-php-ext-install \
  gd \
  intl \
  mbstring \
  mcrypt \
  pdo_mysql \
  xsl \
  zip

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer --version=1.2.0


ENV APP_DIR "/src"
ENV PHPREDIS_VERSION 3.0.0
ENV PHP_MEMORY_LIMIT 1G
ENV PHP_PORT 9000
ENV PHP_PM dynamic
ENV PHP_PM_MAX_CHILDREN 10
ENV PHP_PM_START_SERVERS 4
ENV PHP_PM_MIN_SPARE_SERVERS 2
ENV PHP_PM_MAX_SPARE_SERVERS 6

ENV LARAVEL_QUEUE_WORKER_CONNECTION "sqs"
ENV LARAVEL_QUEUE_WORKER_SLEEP 3
ENV LARAVEL_QUEUE_WORKER_TRIES 3
ENV LARAVEL_QUEUE_WORKER_NUMPROCS 4
ENV LARAVEL_QUEUE_WORKER_TIMEOUT 60



ENV COMPOSER_HOME /home/composer



ENV APP_GIT_REPOSITORY ""
ENV APP_GIT_BRANCH "master"



RUN mkdir -p /root/.ssh


COPY resources/conf/php.ini /usr/local/etc/php/
COPY resources/conf/php-fpm.conf /usr/local/etc/
COPY resources/bin/* /usr/local/bin/
COPY resources/conf/laravel-worker.conf /etc/supervisor/conf.d/

RUN mkdir -p /home/composer
COPY resources/conf/auth.json /home/composer/

# Create dir for www home user, to store .ssh keys.
RUN mkdir -p /var/www

WORKDIR /src

RUN apt-get update && apt-get install -y gcc g++ unzip jq



RUN mkdir -p /usr/src/php/ext/redis \
    && curl -L https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz | tar xvz -C /usr/src/php/ext/redis --strip 1 \
    && echo 'redis' >> /usr/src/php-available-exts \
    && docker-php-ext-install redis

RUN mkdir -p /tmp/envs && touch /tmp/envs/env_file

CMD eval `cat /tmp/envs/env_file`; /usr/local/bin/start-laravel;
