FROM alpine:latest
MAINTAINER Naerymdan <vincent.dev@gmail.com>
##
# PHP 7.X

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk --update add \
        php7-dom \
        php7-ctype \
        php7-curl \
        php7-fpm \
        php7-gd \
        php7-intl \
        php7-json \
        php7-mbstring \
		php7-mcrypt \
        php7-mysqlnd \
        php7-opcache \
        php7-pdo \
        php7-pdo_mysql \
        php7-posix \
        php7-session \
        php7-tidy \
        php7-xml \
        php7-zip \
    && rm -rf /var/cache/apk/*

#Remove useless config
RUN rm -rf /etc/php7/php-fpm.d

#Copy special configs
COPY php.ini         /etc/php7/php.ini
COPY php-fpm.conf    /etc/php7/php-fpm.conf

#Set port
EXPOSE 9000

CMD ["php-fpm7", "-F"]