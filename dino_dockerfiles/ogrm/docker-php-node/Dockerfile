FROM php:7.0-fpm

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs \
            libfreetype6-dev\
            libjpeg62-turbo-dev \
            libpq-dev \
            libpng12-dev \
            sox \
            rsync \
            --no-install-recommends && rm -r /var/lib/apt/lists/*
RUN docker-php-ext-configure gd \
            --with-freetype-dir=/usr/include/ \
            --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd \
            pgsql \
            mbstring
