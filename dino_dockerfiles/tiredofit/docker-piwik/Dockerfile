FROM tiredofit/nginx-php-fpm:8.0
LABEL maintainer="Dave Conroy (github.com/tiredofit)"

ENV CRON_PERIOD=60 \
    NGINX_WEBROOT=/www/html \
    PHP_ENABLE_DOM=TRUE \
    PHP_ENABLE_ICONV=TRUE \
    PHP_ENABLE_IGBINARY=TRUE \
    PHP_ENABLE_LDAP=TRUE \
    PHP_ENABLE_PDO=TRUE \
    PHP_ENABLE_PDO_MYSQL=TRUE \
    PHP_ENABLE_MYSQLND=TRUE \
    PHP_ENABLE_REDIS=TRUE \
    PHP_ENABLE_SIMPLEXML=TRUE \
    PHP_ENABLE_XML=TRUE \
    PHP_ENABLE_XMLREADER=TRUE \
    PHP_ENABLE_CREATE_SAMPLE_PHP=FALSE

RUN set -x && \
    apk update && \
    apk upgrade && \
    rm -rf /var/cache/apk/* /usr/src/*

### Add Files
ADD install /
