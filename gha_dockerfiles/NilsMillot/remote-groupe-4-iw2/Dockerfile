FROM php:5.6.4

RUN apt-get update -qq && \
    apt-get install -qy \
    git \
    gnupg \
    unzip \
    zip && \
    #curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    # composer install
    # composer global require "laravel/lumen-installer=~1.0"
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer
CMD php -S localhost:8001 -t public