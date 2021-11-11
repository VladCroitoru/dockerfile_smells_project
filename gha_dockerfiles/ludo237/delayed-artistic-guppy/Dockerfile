FROM php:8.0-cli-alpine

# Install dev dependencies
RUN apk add --no-cache --virtual .build-deps \
    $PHPIZE_DEPS \
    curl-dev \
    imagemagick-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libtool \
    libxml2-dev \
    oniguruma-dev

# Install production dependencies
RUN apk add --no-cache \
    bash \
    curl \
    freetype-dev \
    g++ \
    gcc \
    git \
    icu-libs \
    icu-dev \
    imagemagick \
    libc-dev \
    libjpeg-turbo \
    libpng \
    libxslt \
    libzip-dev \
    make \
    mysql-client \
    openssh-client \
    rsync \
    zlib-dev

# Install PECL and PEAR extensions
RUN pecl install xdebug

# Configure php extensions
RUN docker-php-ext-configure gd \
    --with-freetype \
    --with-jpeg \
    && docker-php-ext-configure mbstring --enable-mbstring \
    && docker-php-ext-configure intl --enable-intl \
    && docker-php-ext-configure pdo_mysql --with-pdo-mysql \
    && docker-php-ext-configure zip

# Install php extensions
RUN docker-php-ext-install \
    bcmath \
    exif \
    gd \
    intl \
    pdo \
    pdo_mysql \
    pcntl \
    zip

# Enable PECL and PEAR extensions
RUN docker-php-ext-enable intl xdebug

# Install composer
ENV COMPOSER_HOME /composer
ENV PATH ./vendor/bin:/composer/vendor/bin:$PATH
ENV COMPOSER_ALLOW_SUPERUSER 1
RUN curl -s https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin/ --filename=composer

# Install PHP_CodeSniffer
RUN composer global require "squizlabs/php_codesniffer=*"

# Cleanup dev dependencies
RUN apk del -f .build-deps \
    && rm -rf /usr/share/php \
    && rm -rf /tmp/*

# Setup working directory
WORKDIR /var/www