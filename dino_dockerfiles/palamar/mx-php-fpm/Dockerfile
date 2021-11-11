FROM php:7.0.10-fpm
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y g++
RUN apt-get install -y git
RUN apt-get install -y libmcrypt-dev libreadline-dev \
    && docker-php-ext-install -j$(nproc) mcrypt
RUN docker-php-ext-install -j$(nproc) bcmath
RUN apt-get install -y libicu-dev \
    && docker-php-ext-install -j$(nproc) intl
RUN docker-php-ext-install -j$(nproc) mbstring
RUN docker-php-ext-install -j$(nproc) mcrypt
RUN docker-php-ext-install -j$(nproc) hash
RUN apt-get install -y \
    libxml2-dev \
    libxslt-dev \
    && docker-php-ext-install -j$(nproc) simplexml
RUN docker-php-ext-install -j$(nproc) xml
RUN docker-php-ext-install -j$(nproc) xsl
RUN docker-php-ext-install -j$(nproc) soap
RUN docker-php-ext-install -j$(nproc) json
RUN docker-php-ext-install -j$(nproc) dom
RUN apt-get install -y zlib1g-dev \
    && docker-php-ext-install -j$(nproc) zip
RUN docker-php-ext-install -j$(nproc) pdo
RUN docker-php-ext-install -j$(nproc) pdo_mysql
RUN docker-php-ext-install -j$(nproc) gettext
RUN apt-get install -y libbz2-dev \
    && docker-php-ext-install -j$(nproc) bz2
RUN docker-php-ext-install -j$(nproc) iconv
RUN apt-get install -y libcurl3-dev \
    && docker-php-ext-install -j$(nproc) curl
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install opcache
RUN pecl install xdebug
RUN pecl install redis
RUN docker-php-ext-enable redis
COPY ./conf.d/xdebug.ini /usr/local/etc/php/conf.d/
WORKDIR /www/
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN ls -la
RUN ls -la /usr
RUN mv composer.phar /usr/bin/composer
RUN chmod +x /usr/bin/composer
RUN chown -R www-data:www-data /www
RUN mkdir -p /var/www
RUN chown www-data:www-data /var/www
EXPOSE 9000
