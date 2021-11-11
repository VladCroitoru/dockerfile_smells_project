FROM php:7.1-apache

RUN apt-get update && apt-get install curl gnupg wget -y

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
  apt-get install -y nodejs

# Yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN requirements="zlib1g-dev libicu-dev git libpq-dev libmcrypt-dev libxml2-dev libjpeg-dev libpng-dev yarn" \
    && apt-get update && apt-get install -y $requirements \
    && docker-php-ext-install pdo_pgsql \
    && docker-php-ext-install pgsql \
    && docker-php-ext-install intl \
    && docker-php-ext-install zip \
    && docker-php-ext-install mcrypt \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install soap \
    && docker-php-ext-install gd \
    && docker-php-ext-install opcache \
    && docker-php-ext-install bcmath \
    && apt-get purge --auto-remove -y

RUN a2enmod rewrite

ADD config/php.ini /usr/local/etc/php/php.ini

# Install composer
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/bin/composer

RUN mkdir /app
WORKDIR /app

RUN usermod -u 1000 www-data
RUN chown www-data:www-data /app
