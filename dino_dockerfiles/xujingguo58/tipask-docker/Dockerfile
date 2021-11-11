FROM php:7-apache

# Install
RUN sed -i 's/deb.debian.org/debian.ustc.edu.cn/g' /etc/apt/sources.list \
    && apt-get update && apt-get install -y \
	git \
        gcc g++ \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
	zip

RUN docker-php-ext-install -j$(nproc) iconv mcrypt \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install pdo pdo_mysql

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN a2enmod rewrite

ADD apache.conf /etc/apache2/sites-enabled/000-default.conf
ADD php.ini /usr/local/etc/php/

RUN git clone https://github.com/NEUInet/tipask.git

WORKDIR /var/www/html/tipask

RUN composer install 

RUN touch .env && chmod 777 .env
