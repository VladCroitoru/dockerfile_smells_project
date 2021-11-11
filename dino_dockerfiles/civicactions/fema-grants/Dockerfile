FROM php:7.1-apache

# Install Drupal requirements.
RUN apt-get update && apt-get -y install wget libpng-dev mysql-client libbz2-dev git zip unzip && \
    docker-php-ext-install pdo pdo_mysql bz2 gd opcache mbstring zip && \
    a2enmod rewrite && \
    a2enmod headers

# Use /app/src to simplify Drone testing.
RUN sed -i'' 's|/var/www|/app/src|g' /etc/apache2/apache2.conf /etc/apache2/conf-enabled/docker-php.conf /etc/apache2/sites-enabled/000-default.conf

# Add PHP config.
COPY .docker/php-docker.ini /usr/local/etc/php/conf.d

# Install PHP Composer.
COPY .docker/getcomposer.sh /usr/local/bin
RUN /usr/local/bin/getcomposer.sh
ENV PATH="$PATH:/app/src/vendor/bin"

# Copy in code so this can be used as a production image also.
COPY . /app/src
WORKDIR /app/src/web

# Custom entrypoint.
COPY .docker/docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
