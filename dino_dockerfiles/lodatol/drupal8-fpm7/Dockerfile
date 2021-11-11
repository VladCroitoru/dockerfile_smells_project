FROM php:7-fpm
MAINTAINER lodatoluciano@gmail.com

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg-dev \ 
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libpq-dev \
        sqlite \
        mysql-client \ 
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr --with-jpeg-dir=/usr  --with-png-dir=/usr \
    && docker-php-ext-install -j$(nproc) gd mbstring opcache pdo pdo_mysql pdo_pgsql zip

COPY php-drupal8-configs /usr/local/etc/php/conf.d

WORKDIR /tmp

RUN \
curl -sS https://getcomposer.org/installer | php && \
mv composer.phar /usr/local/bin/composer && \
ln -s /usr/local/bin/composer /usr/bin/composer && \
composer global require drush/drush:~8

RUN echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> ~/.bashrc

#needed by drush
RUN apt-get install -y wget git 

#addind uploadprogress
ADD pecl-php-uploadprogress pecl-php-uploadprogress
WORKDIR pecl-php-uploadprogress
RUN pecl install package.xml && echo "extension=uploadprogress.so" >> /usr/local/etc/php/conf.d/uploadprogress.ini

WORKDIR /var/www/html/
