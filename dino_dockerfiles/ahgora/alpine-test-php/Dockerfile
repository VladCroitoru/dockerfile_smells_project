FROM alpine:3.4

RUN apk update && apk add --no-cache wget curl make gcc g++ python linux-headers paxctl libgcc libstdc++ gnupg libc6-compat bind-tools apache2=2.4.27-r0 apache2-utils=2.4.27-r0 php5-apache2 php5-gettext php5-cgi php5-gd php5-intl php5-mcrypt patch php5-imap php5-json php5-phar php5-openssl=5.6.31-r0 openssl php5-xml


RUN wget https://phar.phpunit.de/phpunit-4.8.9.phar && chmod +x phpunit-4.8.9.phar && mv phpunit-4.8.9.phar /usr/local/bin/phpunit &&\
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-php5-mongo/master/sgerrand.rsa.pub &&\
    wget https://github.com/sgerrand/alpine-pkg-php5-mongo/releases/download/1.16.4-r0/php5-mongo-1.6.14-r0.apk &&\
    apk add php5-mongo-1.6.14-r0.apk &&\
    apk add fabric  --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted &&\
    apk del wget curl &&\
    rm /var/cache/apk/*

ADD config.php /etc/config_pw2/config.php
ADD auth.rsa.pub /etc/config_pw2/auth.rsa.pub
ADD auth.rsa /etc/config_pw2/auth.rsa
