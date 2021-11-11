FROM webdevops/php-nginx-dev:7.4
LABEL maintainer="Alexander Garzon <agarzon@php.net>"

RUN apt-get update

# ioncube for PHP 7.4
ADD https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz /tmp/
RUN cd /tmp/ && tar xvfz /tmp/ioncube_loaders_lin_x86-64.tar.gz
RUN cp /tmp/ioncube/ioncube_loader_lin_* /usr/local/lib/php/extensions/no-debug-non-zts-20190902/
RUN echo "zend_extension = /usr/local/lib/php/extensions/no-debug-non-zts-20190902/ioncube_loader_lin_7.2.so" > /usr/local/etc/php/conf.d/01-ioncube.ini
RUN rm -rf /tmp/ioncube/

# PHPUNIT
ADD https://phar.phpunit.de/phpunit.phar /usr/local/bin/phpunit
RUN chmod +x /usr/local/bin/phpunit

# clear
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
