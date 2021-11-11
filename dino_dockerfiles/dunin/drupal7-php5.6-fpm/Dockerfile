FROM php:5.6-fpm

MAINTAINER Alexander Dunin <a@dunin.by>

RUN apt-get update

RUN apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng12-dev \
    libmcrypt-dev \
    libxslt-dev \
    libicu-dev \
    unzip \
    libgeoip-dev \
    nano \
    mysql-client

RUN rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install \
    opcache \
    exif \
    dba \
    gd \
    mcrypt \
    iconv \
    mbstring \
    pdo_mysql \
    mysqli \
    soap \
    zip \
    xsl \
    xmlrpc
    
RUN usermod -u 1000 www-data    

COPY ./conf/php.ini /usr/local/etc/php/php.ini
COPY ./conf/php.conf /usr/local/etc/php-fpm.d/php.conf

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');" \
    && mv composer.phar /usr/local/bin/composer

RUN php -r "readfile('http://files.drush.org/drush.phar');" > drush \
    && chmod +x drush \
    && mv drush /usr/local/bin

RUN drush dl registry_rebuild-7.x
