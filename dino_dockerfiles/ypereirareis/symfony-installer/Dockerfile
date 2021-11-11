FROM php:7.1.5-fpm-alpine

MAINTAINER Yannick Pereira-Reis <yannick.pereira.reis@gmail.com>

ENV HOME /app
WORKDIR /app

RUN curl -LsS http://symfony.com/installer -o /usr/local/bin/symfony && \
    chmod a+x /usr/local/bin/symfony && \
    echo "date.timezone = Europe/Paris" >> /usr/local/etc/php/conf.d/symfony.ini

ENTRYPOINT ["symfony"]

CMD []
