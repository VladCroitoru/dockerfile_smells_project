# Use an official PHP runtime as a base image
FROM hexaua/dev

# ADD copyright
LABEL maintainer "a.ohanov@hexa.com.ua"

# Install any needed packages
RUN pecl install xdebug-2.5.0 \
    && docker-php-ext-enable xdebug

RUN apt-get purge -y g++ \
    && apt-get autoremove -y \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

