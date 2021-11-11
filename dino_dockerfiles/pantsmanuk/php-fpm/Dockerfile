FROM php:7.0-fpm

MAINTAINER Murray Crane <murray.crane@gmail.com>

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && apt-get -y install mcrypt libmcrypt4 libmcrypt-dev nullmailer && echo php-fpm.docker.local > /etc/mailname

RUN docker-php-ext-install -j$(nproc) mcrypt mysqli

RUN echo sendmail_path=/usr/sbin/sendmail -t -i > /usr/local/etc/php/php.ini
