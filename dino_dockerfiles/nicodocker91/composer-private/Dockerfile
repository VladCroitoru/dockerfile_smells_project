FROM php:7.1-fpm-alpine

MAINTAINER "Nicolas Giraud" <nicolas.giraud.dev@gmail.com>

# Set correct environment variables for composer.
ENV COMPOSER_MEMORY_LIMIT=-1 COMPOSER_VENDOR_DIR=vendor COMPOSER_CACHE_DIR=/tmp/.composer

# Install the latest version of composer.
RUN curl -Ls https://getcomposer.org/installer > /tmp/installer && \
    if [ "$(curl -Ls https://composer.github.io/installer.sig)" != $(php -r "echo hash_file('SHA384', '/tmp/installer');") ]; \
    then \
        >&2 echo 'ERROR: Invalid installer signature' \
        rm -rf /tmp/* \
        exit 1; \
    fi && \
    php /tmp/installer --no-ansi --install-dir=/usr/local/bin --filename=composer && \

    # Use the project hirak/prestissimo to run composer in parallel
    composer global require hirak/prestissimo && \

    # Install git to be able to composer to fetch local repositories.
    apk add --no-cache --virtual .tools git openssh && \
    # Install freetype-dev that is required for the "zip" extension.
    apk add --no-cache --virtual .dev-packages freetype-dev && \
    # Download and install all PHP extensions needed.
    apk add --no-cache --virtual .packages zip bzip2 && \

    # Install and enable PHP extension that are required for common composer packages.
    docker-php-ext-install zip pcntl bcmath pdo pdo_mysql mbstring && \
    docker-php-ext-enable zip pcntl bcmath pdo pdo_mysql mbstring && \

    # Purge apk and useless files.
    apk del --purge .dev-packages .packages && \

    rm -rf /var/lib/apt/lists/* /var/cache/apk/* /tmp/*

VOLUME ["/var/"]
WORKDIR /var/www

ENTRYPOINT ["composer"]
