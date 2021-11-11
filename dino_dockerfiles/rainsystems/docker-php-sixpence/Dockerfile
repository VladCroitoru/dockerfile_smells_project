FROM php:5-apache

RUN a2enmod rewrite && \
    a2enmod env && \
    apt-get update -y && apt-get install -y \
    libpq-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    ruby \
    imagemagick \
    libmemcached-dev \
    npm \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    docker-php-ext-configure pdo_pgsql && \
    docker-php-ext-install pdo pdo_pgsql mbstring bcmath zip gd exif && \
    gem install -n /usr/bin sass && \
    pecl install memcached apcu-4.0.8 && \
    ln -s /usr/bin/nodejs /usr/bin/node && \
    curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    rm -rf /var/www/* /etc/apache2/sites-enabled/000-default.conf


