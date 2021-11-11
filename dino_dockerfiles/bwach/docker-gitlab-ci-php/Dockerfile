# for unit tests cli is enough, if not, you can switch it to -apache version
FROM php:5.6.26-cli

# default timezone setting which is missing in the image
RUN echo "date.timezone=Europe/Warsaw" >> /usr/local/etc/php/php.ini

# composer installed globally
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# zip binary
# https://github.com/docker-library/php/issues/61
# it should work with just "docker-php-ext-instal", but it doesn't
RUN apt-get update && \
    apt-get install -y \
        zlib1g-dev && \
    docker-php-ext-install zip
