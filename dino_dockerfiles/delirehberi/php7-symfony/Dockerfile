FROM php:7.4-fpm
RUN apt-get update && apt-get install -y \
      libfreetype6-dev \
      libjpeg62-turbo-dev \
      libpng-dev \
      zlib1g-dev \
      libicu-dev \
      libpq-dev \
      libzip-dev \
      g++ \
      libcurl4-gnutls-dev \ 
      libonig-dev

RUN docker-php-ext-install -j$(nproc) iconv \
      && docker-php-ext-configure gd \ 
      && docker-php-ext-install -j$(nproc) gd \
      && docker-php-ext-install -j$(nproc) pdo \
      && docker-php-ext-install -j$(nproc) exif \
      && docker-php-ext-configure intl \
      && docker-php-ext-configure pdo_pgsql \
      && docker-php-ext-install -j$(nproc) intl \
      && docker-php-ext-install -j$(nproc) pdo_pgsql \
      && docker-php-ext-install -j$(nproc) mysqli \
      && docker-php-ext-install -j$(nproc) bcmath \
      && docker-php-ext-install -j$(nproc) curl \
      && pecl install zip \
      && docker-php-ext-enable zip \
      && docker-php-ext-install -j$(nproc) pdo_mysql 

#its required for composer
RUN apt-get install -y git

RUN pecl install -o -f redis \
	&&  rm -rf /tmp/pear \
	&&  docker-php-ext-enable redis
##composer
WORKDIR "/tmp"

RUN php -r "readfile('https://getcomposer.org/installer');" > composer-setup.php
RUN php composer-setup.php --install-dir=/bin --filename=composer
RUN php -r "unlink('composer-setup.php');"


WORKDIR "/app"
RUN usermod -u 1000 www-data

CMD ["php-fpm"]
