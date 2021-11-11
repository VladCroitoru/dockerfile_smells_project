FROM alpine:latest
MAINTAINER Etopian Inc. <contact@etopian.com>

RUN apk update && apk upgrade && \
  apk add \
    openssl \
    ca-certificates \
    curl \
    bash \
    bash-completion \
    ncurses \
    vim \
    gettext \
    logrotate \
    tar \
    rsync \
    shadow \
    s6 \
    nginx \
    mailcap \
    php7-apcu \
    php7-dev \
    php7-bcmath \
    php7-fpm \
    php7-ctype \
    php7-curl \
    php7-dom \
    php7-gd \
    php7-gettext \
    php7-gmp \
    php7-iconv \
    php7-intl \
    php7-json \
    php7-mcrypt \
    php7-mysqli \
    php7-openssl \
    php7-opcache \
    php7-pdo \
    php7-pdo_mysql \
    php7-pear \
    php7-pgsql \
    php7-phar \
    php7-mcrypt \ 
    php7-exif \
    php7-xmlreader \
    php7-sqlite3 \
    php7-xml \
    php7-xsl \
    php7-dom \
    php7-zip \
    php7-dev \
    php7-mbstring \
    php7-session \
    php7-apcu \
    php7-simplexml \
    autoconf \
    build-base \
    libsodium-dev \
    git \
    dcron \
    php7-zlib && \
    rm -rf \
      /var/cache/apk/* && \
    rm -rf \
      /etc/nginx/* && \
  mkdir /etc/logrotate.docker.d


ENV TERM=xterm PHP_MEMORY_LIMIT=512M PHP_POST_MAX_SIZE=2G PHP_UPLOAD_MAX_FILESIZE=2G PHP_MAX_EXECUTION_TIME=3600 PHP_MAX_INPUT_TIME=3600 PHP_DATE_TIMEZONE=UTC PHP_LOG_LEVEL=warning PHP_MAX_CHILDREN=75 PHP_MAX_REQUESTS=500 PHP_PROCESS_IDLE_TIMEOUT=10s NGINX_WORKER_PROCESSES=5 NGINX_WORKER_CONNECTIONS=4096 NGINX_SENDFILE=on NGINX_TCP_NOPUSH=on LOGSTASH_ENABLED=false  HOST_FRONT=frontend.dev HOST_BACK=backend.dev DB_NAME=user DB_USER=user DB_PASS=pass DB_PORT=3306 DB_HOST=172.17.0.1 REDIS_HOST=172.17.0.1 REDIS_PORT=6379 REDIS_DB=0


ADD rootfs /

COPY nginx.conf /etc/nginx/nginx.conf
COPY yii2nginx.conf /etc/nginx/presets/default.conf
COPY setup /etc/s6/nginx/setup

RUN  sed -ie 's/-n//g' /usr/bin/pecl && pecl install libsodium && pecl install redis && curl -sS https://getcomposer.org/installer \
  | php -- --install-dir=/usr/bin --filename=composer


EXPOSE 80

WORKDIR /app
CMD ["/bin/s6-svscan", "/etc/s6"]



