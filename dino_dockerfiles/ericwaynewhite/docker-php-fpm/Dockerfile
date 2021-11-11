FROM alpine:latest
MAINTAINER eric.white@gmail.com

ENV LANG='en_US.UTF-8' \
    LANGUAGE='en_US.UTF-8' \
    TERM='xterm'

RUN apk -U upgrade && \
    apk -U add --no-cache \
        apache2-proxy \
        php7-fpm \
        php7 \
        php7-opcache \
        php7-phar \
        php7-json \
        php7-iconv \
        php7-xml \
        php7-simplexml \
        php7-mbstring \
        php7-openssl \
        php7-pdo \
        php7-ldap \
        php7-gd \
        php7-curl \
        php7-ctype \
        php7-dom \
        php7-common \
        php7-pdo_mysql \
        php7-session \
        php7-soap \
        grep \
        git \
        curl \
        vim

RUN  rm -rf /etc/init.d/*; \
     mkdir /run/apache2; \
     addgroup -g 1000 -S site; \
     adduser -G site -u 1000 -s /bin/sh -D site; \
     sed -rie 's|;error_log = log/php7/error.log|error_log = /dev/stdout|g' /etc/php7/php-fpm.conf 

VOLUME ["/web"]

EXPOSE 80

COPY httpd.conf /etc/apache2/httpd.conf
COPY www.conf /etc/php7/php-fpm.d/www.conf
COPY php.ini /etc/php7/php.ini
COPY scripts /scripts

RUN chmod -R 755 /scripts

CMD ["/scripts/run.sh"]

