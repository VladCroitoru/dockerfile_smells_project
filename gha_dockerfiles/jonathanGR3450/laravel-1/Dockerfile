FROM php:7.4-fpm

# copia composer.lock y composer.json a la carpeta /var/www/
COPY composer.lock composer.json /var/www/

# directorio de trabajo
WORKDIR /var/www

# Install dependencies
RUN apt-get update && pecl install redis && apt-get install -y  --no-install-recommends \
    libzip-dev \
    libonig-dev \
    libpq-dev \
    build-essential \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    locales \
    zip \
    jpegoptim optipng pngquant gifsicle \
    vim \
    unzip \
    git \
    curl

# clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# install extensions
RUN docker-php-ext-install pdo pdo_pgsql zip exif pcntl
RUN docker-php-ext-configure gd --with-jpeg=/usr/include/ --with-freetype=/usr/include/
RUN docker-php-ext-install gd
RUN docker-php-ext-enable redis

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Add user for laravel application
RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www

# copia el codigo a la carpeta /var/www
COPY . /var/www

# copia el codigo a la carpeta con permisos de ususario
COPY --chown=www:www . /var/www

USER www

EXPOSE 9000
CMD [ "php-fpm" ]