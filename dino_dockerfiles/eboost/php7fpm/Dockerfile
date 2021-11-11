FROM php:7-fpm

# Install modules
RUN apt-get update && apt-get install -y \
        imagemagick \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libicu-dev \
        libsqlite-dev \
        libsqlite3-dev \
        libmagickwand-dev \
        libmagickcore-dev

RUN pecl install imagick

# Install php extensions
RUN docker-php-ext-install intl iconv mcrypt pdo pdo_mysql pdo_sqlite tokenizer\
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install opcache \
    && docker-php-ext-install zip \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install exif \
    && docker-php-ext-enable imagick \
    && docker-php-ext-install bcmath

# soap
RUN buildRequirements="libxml2-dev" \
	&& apt-get update && apt-get install -y ${buildRequirements} \
	&& docker-php-ext-install soap \
	&& apt-get purge -y ${buildRequirements} \
	&& rm -rf /var/lib/apt/lists/*

CMD ["php-fpm"]
