FROM php:7.1.8-apache

RUN docker-php-ext-install mbstring pdo pdo_mysql

RUN apt-get update && apt-get install -y \
    curl \
    mysql-client \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /hotline \
    && wget https://github.com/sharett/hotline/archive/master.tar.gz \
    && tar -xzf master.tar.gz -C /hotline --strip=1 \
    && rm -f master.tar.gz

WORKDIR "/hotline"

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer install --no-interaction

COPY ./vhost.conf /etc/apache2/sites-available/000-default.conf
RUN chown -R www-data:www-data /hotline