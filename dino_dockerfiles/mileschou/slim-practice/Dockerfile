FROM php:7.0-apache
MAINTAINER MilesChou <jangconan@gmail.com>

# Install Extensions
RUN set -xe && \
        apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
            zlib1g-dev \
        && docker-php-ext-install \
            zip \
        && rm -r /var/lib/apt/lists/*

# Install Composer
RUN set -xe && \
        php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
        php -r "if (hash_file('SHA384', 'composer-setup.php') === 'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
        php composer-setup.php && \
        php -r "unlink('composer-setup.php');" && \
        mv composer.phar /usr/local/bin/composer

# Apache2 setting
RUN set -xe && \
        a2enmod rewrite && \
        sed -i "s/DocumentRoot.*/DocumentRoot \/var\/www\/html\/public/g" /etc/apache2/sites-enabled/000-default.conf

COPY composer.json ./
COPY composer.lock ./
COPY .env.example ./
RUN composer install --no-dev --optimize-autoloader

COPY . ./
