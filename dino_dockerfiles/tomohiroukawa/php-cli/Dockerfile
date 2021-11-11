FROM php:5.6-cli

WORKDIR /php

RUN apt-get update && apt-get install -y git zip

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
RUN composer global require hirak/prestissimo

RUN pecl install xdebug-2.5.4
RUN echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20131226/xdebug.so" >> /usr/local/etc/php/conf.d/xdebug.ini

RUN apt-get update && apt-get install -y git zip

CMD ["tail", "-f", "/dev/null"]
