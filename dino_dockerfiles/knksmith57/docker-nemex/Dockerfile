FROM alpine:3.2
MAINTAINER Kyle Smith <knksmith57@gmail.com>

##
## nginx + php-fm setup from psi-4ward/docker-php-nginx. with a few tweaks.
##

RUN apk --update add \
    ca-certificates nginx openssl tar wget \
    php-fpm php-json php-zlib php-xml php-pdo php-phar php-openssl \
    php-pdo_mysql php-mysqli \
    php-gd php-iconv php-mcrypt

## via psi-4ward/docker-php-nginx:
## fix php-fpm "Error relocating /usr/bin/php-fpm: __flt_rounds: symbol not found" bug
RUN apk --update add musl

RUN rm -rf /var/cache/apk/*

## nginx + php-fm files from psi-4ward/docker-php-nginx
ADD files/nginx.conf /etc/nginx/
ADD files/php-fpm.conf /etc/php/
ADD files/run.sh /

## install dockerize
RUN wget -O /tmp/dockerize-v0.0.4.tar.gz \
      'https://github.com/jwilder/dockerize/releases/download/v0.0.4/dockerize-linux-amd64-v0.0.4.tar.gz' \
    && tar -C /usr/local/bin -xzvf '/tmp/dockerize-v0.0.4.tar.gz'

## install nemex, pinned to commit d26d2d6 for stability
RUN wget -O /tmp/nemex-v1.0.tar.gz \
      'https://github.com/neonelephantstudio/nemex/archive/v1.0.tar.gz' \
    && tar -C /tmp -xzvf '/tmp/nemex-v1.0.tar.gz'

RUN mkdir -p /app \
    && cp -R /tmp/nemex-1.0/* /app/

## per nemex docs, need projects directory with permissions 777
RUN mkdir /app/projects \
    && chmod 777 /app/projects

## nemex config template
ADD config.php.tmpl /app/config.php.tmpl


WORKDIR /app
EXPOSE 80


CMD dockerize \
    -template /app/config.php.tmpl:/app/config.php \
    /run.sh

