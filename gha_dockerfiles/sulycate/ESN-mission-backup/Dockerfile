FROM php:5.6-fpm

# Copy composer.lock and composer.json
COPY blog/composer.lock blog/composer.json /var/www/

# Set working directory
WORKDIR /var/www

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    locales \
    curl \
    libmemcached11 \
    libmemcachedutil2 \
    libmemcached-dev 

# Install X-Debug
RUN pecl install xdebug-2.5.5 && docker-php-ext-enable xdebug

# Install memcached
RUN pecl install memcached-2.2.0
RUN echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install extensions
RUN docker-php-ext-install pdo_mysql mbstring zip exif pcntl
RUN docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/
RUN docker-php-ext-install gd

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Copy existing application directory contents
COPY blog/ /var/www/

EXPOSE 9000

CMD ["php-fpm"]