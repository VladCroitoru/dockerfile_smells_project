FROM mogria/3source-base:latest

MAINTAINER "Mogria <m0gr14@gmail.com>"

RUN apk add --update \
    php-cli \
    php-ctype \
    php-dom \
    php-gd \
    php-json \
    php-mcrypt \
    php-mysql \
    php-openssl \
    php-pdo \
    php-pdo_mysql \
    php-phar

ENTRYPOINT ["umask-wrapper.sh", "container-user.sh", "php"]
    
