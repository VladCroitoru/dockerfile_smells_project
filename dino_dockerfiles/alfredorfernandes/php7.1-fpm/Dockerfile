FROM php:7.1-fpm

RUN apt-get update && \
    apt-get dist-upgrade -y  && \
    apt-get install -y \
            curl \
            git \
            git-core \
            wget \
            imagemagick \
            libxml2-dev \
            zlib1g-dev

RUN docker-php-ext-install json \
 && docker-php-ext-install dom \
 && docker-php-ext-install bcmath \
 && docker-php-ext-install mbstring \
 && docker-php-ext-install pdo_mysql \
 && docker-php-ext-install pcntl \
 && docker-php-ext-install opcache \
 && docker-php-ext-install zip \
 && docker-php-ext-install soap


# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# Permissions
RUN usermod -u 1000 www-data
RUN chown -R www-data:www-data /var/www/html
