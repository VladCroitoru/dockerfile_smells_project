FROM php:7.0-apache

# Install Required Packages
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
    git \
    zlib1g-dev \
    && rm -r /var/lib/apt/lists/*


# Install Extensions
RUN docker-php-ext-install pdo_mysql zip

# Install Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === 'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/local/bin/composer

COPY ./composer.json ./
COPY ./composer.lock ./
COPY ./.env.example ./
RUN composer install --no-dev

COPY ./src ./src
COPY ./public ./public

# Apache2 setting
RUN a2enmod rewrite
RUN sed -i "s/DocumentRoot.*/DocumentRoot \/var\/www\/html\/public/g" /etc/apache2/sites-enabled/000-default.conf
