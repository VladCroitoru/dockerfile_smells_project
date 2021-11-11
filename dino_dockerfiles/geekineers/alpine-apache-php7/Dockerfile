FROM alpine:latest

MAINTAINER geekineers <developers@8layertech.com>

RUN apk update && apk upgrade && \
    apk add --no-cache \
                        curl  \ 
                        openssl \
                        wget \
                        php7 \
                        php7-bcmath \
                        php7-apache2 \
                        php7-openssl \
                        php7-dom \
                        php7-pdo_mysql \ 
                        php7-fpm \
                        php7-mysqli \
                        php7-pgsql \
                        php7-sqlite3 \
                        php7-phar \
                        php7-mbstring \
                        php7-apcu \
                        php7-intl \
                        php7-mcrypt \
                        php7-json \
                        php7-gd \ 
                        php7-curl \
                        php7-xml \
                        php7-xmlreader \
                        php7-ctype \
                        php7-session

RUN ln -s /etc/php7 /etc/php && \
    ln -s /usr/bin/php7 /usr/bin/php && \
    ln -s /usr/lib/php7 /usr/lib/php

RUN wget https://phar.phpunit.de/phpunit-6.0.phar && \
    chmod +x phpunit-6.0.phar && \
    mv phpunit-6.0.phar /usr/local/bin/phpunit

RUN cd /tmp && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer

RUN sed -i 's/AllowOverride None/AllowOverride All/g' /etc/apache2/httpd.conf && \
    sed -i 's/AllowOverride none/AllowOverride All/g' /etc/apache2/httpd.conf && \
    sed -i 's/\/var\/www\/localhost\/htdocs/\/var\/www\/app\/public/g' /etc/apache2/httpd.conf && \
    sed -i 's/\#LoadModule rewrite_module/LoadModule rewrite_module/g' /etc/apache2/httpd.conf

COPY httpd-foreground /usr/local/bin/

RUN chmod 755 /usr/local/bin/httpd-foreground
RUN mkdir /var/www/localhost/app

EXPOSE 80 443

ENTRYPOINT ["httpd-foreground"]