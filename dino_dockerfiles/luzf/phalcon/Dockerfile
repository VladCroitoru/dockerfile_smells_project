FROM php:5.6-fpm

RUN docker-php-ext-install pdo pdo_mysql opcache

RUN apt-get update \
    && apt-get install -y libicu-dev libfreetype6-dev libjpeg62-turbo-dev libpng12-dev git

RUN docker-php-ext-install intl

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN docker-php-ext-install zip

RUN usermod -u 1000 www-data

RUN git clone git://github.com/phalcon/cphalcon.git -b 2.0.x
RUN cd cphalcon/build/ && \
    ./install && \
    cd /tmp && \
    /bin/rm -rf /tmp/cphalcon/

RUN docker-php-ext-enable phalcon

WORKDIR /var/www