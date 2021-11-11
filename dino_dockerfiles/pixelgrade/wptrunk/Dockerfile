FROM wordpress:cli-php7.1

WORKDIR /tmp/wordpress/

USER root

## Install PhpUnit
RUN curl -SL --insecure "https://phar.phpunit.de/phpunit.phar" -o phpunit.phar \
    && chmod +x phpunit.phar \
    && mv phpunit.phar /usr/bin/phpunit


# Install composer global bin
#RUN curl -sSL https://phar.phpunit.de/phpunit-5.7.phar -o phpunit.phar && \
#    chmod +x phpunit.phar && \
#    mv phpunit.phar /usr/local/bin/phpunit

#USER www-data

RUN apk update \
    && apk add  --no-cache git mysql-client curl libmcrypt libmcrypt-dev \
    libxml2-dev freetype-dev libpng-dev libjpeg-turbo-dev g++ make autoconf \
    && apk add rsync \
    && docker-php-source extract \
    && pecl install xdebug redis \
    && docker-php-ext-enable xdebug redis \
    && docker-php-source delete \
    && docker-php-ext-install mcrypt pdo_mysql soap \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && rm -rf /tmp/*

ADD /tests/phpunit/ /tmp/wordpress-tests-lib/

ADD src/ /tmp/wordpress/
ADD tests /tmp/tests/
ADD tools /tmp/tools/
ADD .jshintrc /tmp/.jshintrc
ADD Gruntfile.js /tmp/Gruntfile.js
ADD package.json /tmp/package.json
ADD phpunit.xml.dist /tmp/phpunit.xml.dist
ADD wp-cli.yml /tmp/wp-cli.yml
ADD wp-tests-config.php /tmp/wp-tests-config.php
ADD wp-tests-config.php /tmp/wordpress-tests-lib/wp-tests-config.php

EXPOSE 9000
