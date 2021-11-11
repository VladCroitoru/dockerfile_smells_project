FROM php:8-fpm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpq-dev \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install PHP extensions
RUN docker-php-ext-install pgsql pdo pdo_pgsql mbstring exif pcntl bcmath gd

# Get latest Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Create system user to run Composer and Artisan Commands
RUN useradd -G www-data,root -u 1000  -d  /home/vinicius vinicius
RUN mkdir -p /home/vinicius/.composer && \
    chown -R vinicius:vinicius /home/vinicius

# Set working directory 
WORKDIR /var/www

COPY . .

RUN composer install

EXPOSE 8001
