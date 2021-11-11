FROM php:7.2

# Install dependencies
RUN apt-get update && \
    apt-get install -y git \
    zip \
    libjpeg-dev \
    libpng-dev \
    libpq-dev \
    zlib1g-dev \
    libzip-dev \
    libxpm-dev

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install extensions
RUN docker-php-ext-install pdo_mysql pdo_pgsql mbstring exif pcntl zip
RUN docker-php-ext-configure gd --with-gd --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/
RUN docker-php-ext-install gd

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
