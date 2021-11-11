FROM kolyadin/php:72

MAINTAINER Aleksey Kolyadin <donflash@gmail.com>

RUN sudo apt-get update \
    && sudo apt-get install -y libevent-dev libssl-dev \
    && sudo pecl install event \
    && echo "extension=event.so" > /usr/local/etc/php/conf.d/event.ini

RUN composer require -o workerman/workerman

EXPOSE 2346