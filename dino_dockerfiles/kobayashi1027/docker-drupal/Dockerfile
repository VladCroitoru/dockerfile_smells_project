# from https://www.drupal.org/requirements/php#drupalversions
FROM php:7.0-apache
MAINTAINER Hiroaki Kobayashi <koba1027yasho@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

# Setup apache
RUN rm -rf /var/www/html
RUN sed -i 's/DocumentRoot.*/DocumentRoot \/var\/www\/drupal\/web/' /etc/apache2/sites-available/000-default.conf
RUN a2ensite 000-default && a2enmod rewrite

# Install packages and PHP extensions
RUN apt-get update && apt-get install -y \
    libpng12-dev \
    libjpeg-dev \
    libpq-dev \
    git \
    mysql-client \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install gd mbstring opcache pdo pdo_mysql pdo_pgsql zip \
    && apt-get clean

# Set recommended PHP.ini settings
# See https://secure.php.net/manual/en/opcache.installation.php
RUN { \
    echo 'opcache.memory_consumption=128'; \
    echo 'opcache.interned_strings_buffer=8'; \
    echo 'opcache.max_accelerated_files=4000'; \
    echo 'opcache.revalidate_freq=60'; \
    echo 'opcache.fast_shutdown=1'; \
    echo 'opcache.enable_cli=1'; \
} > /usr/local/etc/php/conf.d/opcache-recommended.ini

# Install composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Install drupal 8
ENV COMPOSER_ALLOW_SUPERUSER 1
RUN composer create-project drupal-composer/drupal-project:8.x-dev /var/www/drupal --stability dev --no-interaction
RUN chown -R www-data:www-data /var/www

# Archive drupal directory (for pre-seeding)
WORKDIR /var/www/drupal
RUN tar zcvf ~/drupal.tar.gz .

# Set path of drush and drupal command
ENV PATH /var/www/drupal/vendor/bin:$PATH

# Set volumes
VOLUME /var/www/drupal

COPY start-drupal /usr/local/bin/
CMD ["start-drupal"]
