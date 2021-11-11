FROM wordpress

# zlib is needed by php-ext zip
RUN apt-get update && \
    apt-get install -y \
        libzip-dev \
        zlib1g-dev

# needed by some plugins
RUN docker-php-ext-install \
    zip \
    exif

