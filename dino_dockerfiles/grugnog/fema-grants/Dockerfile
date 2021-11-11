FROM php:7.1-apache

# Install Drupal requirements.
RUN apt-get update && apt-get -y install wget libpng-dev mysql-client libbz2-dev git zip unzip && \
    docker-php-ext-install pdo pdo_mysql bz2 gd opcache mbstring zip

# Enable apache mod rewrite for clean urls.
RUN a2enmod rewrite

# Add PHP config.
COPY .docker/php-docker.ini /usr/local/etc/php/conf.d

# Install PHP Composer.
COPY .docker/getcomposer.sh /usr/local/bin
RUN /usr/local/bin/getcomposer.sh
ENV PATH="$PATH:/var/www/vendor/bin"

# Copy in code so this can be used as a production image also.
COPY . /var/www

# Custom entrypoint.
COPY .docker/docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
