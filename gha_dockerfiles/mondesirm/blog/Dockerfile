FROM php:8-apache

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
    libcurl3-openssl-dev \
    zlib1g-dev \
    libmemcached-dev \
    && pecl install memcached-3.1.5 \
    && docker-php-ext-enable memcached

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/* \
&& sed -i 's|DocumentRoot /var/www/html|DocumentRoot /var/www/html/public|g' /etc/apache2/sites-available/*.conf

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql

RUN a2enmod rewrite

# Set working directory
WORKDIR /var/www/html

RUN chown -R www-data:www-data /var/www/html

# Get latest Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer
