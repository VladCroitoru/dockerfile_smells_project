FROM php:7.4-fpm

COPY composer.lock composer.json /var/www/

#Set working directory
WORKDIR /var/www

#Install dependecies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
    vim

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

#Install Php Extension
RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd

#Get latest Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Copy existing application directory contents to the working directory
COPY --chown=www-data:www-data . /var/www
RUN chmod -R 755 /var/www/storage

RUN composer install --optimize-autoloader --no-dev
RUN composer dump-autoload -o

# COPY --chown=www-data:www-data .env.example .env
# RUN php artisan key:generate && php artisan jwt:secret

RUN php artisan cache:clear
RUN php artisan config:clear

#EXPOSE 9000
#CMD ["php-fpm"]
