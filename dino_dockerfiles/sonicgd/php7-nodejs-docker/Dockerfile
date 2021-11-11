FROM php:7.1-cli

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

RUN apt install -y \
    libxml2-dev \
    zlib1g-dev \
    libfreetype6 \
    libfreetype6-dev \
    libjpeg62-turbo \
    libjpeg-dev \
    libpng12-0 \
    libpng-dev \
    libxslt1.1 \
    libxslt-dev \
    libpq5 \
    libpq-dev \
    wget \
    zip \
    git \
    nodejs \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install pdo_pgsql pgsql soap zip gd pdo_mysql mysqli \
    && apt purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
        autoconf \
        binutils \
        gcc \
        libc-dev \
        g++ \
        make \
        libxml2-dev \
        zlib1g-dev \
        libfreetype6-dev \
        libjpeg-dev \
        libpng-dev \
        libxslt-dev \
        libxml2-dev \
        libpq-dev \
        libicu-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

    RUN  curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin -- --filename=composer
