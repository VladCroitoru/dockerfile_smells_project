FROM php:7.4-fpm

# arguments defined in docker-compose.yml
ARG user
ARG uid

#install sytem dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip

#clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

#install php extensions
RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd sockets

#get latest composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

#create system user to run composer and artisan commands
RUN useradd -G www-data,root -u $uid -d /home/$user $user
RUN mkdir -p /home/$user/.composer && chown -R $user:$user /home/$user

# install redis
RUN pecl install -o -f redis \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable redis

WORKDIR /var/www

USER $user
