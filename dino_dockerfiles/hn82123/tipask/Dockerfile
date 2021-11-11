FROM php:7-apache

# Install
RUN   apt-get update && apt-get install -y \
	git \
        gcc g++ \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        zip \
     && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-install -j$(nproc) iconv mcrypt \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) gd; \ 
  docker-php-ext-install pdo pdo_mysql; \
  curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer; \
  a2enmod rewrite

ADD apache.conf /etc/apache2/sites-enabled/000-default.conf
ADD php.ini /usr/local/etc/php/

WORKDIR /var/www/html/
RUN git clone https://github.com/NEUInet/tipask.git

WORKDIR /var/www/html/tipask

RUN composer install; \
    touch .env && chown www-data -R .env storage bootstrap/cache
