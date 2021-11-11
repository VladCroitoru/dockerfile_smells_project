# Dockerfile for development environment
FROM php:8.0

ARG USER=1000:1000

ARG MAX_UPLOAD_FILESIZE=256
ENV MAX_UPLOAD_FILESIZE=${MAX_UPLOAD_FILESIZE}

# Install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    # Install common dependencies
    apt-get install -y git ffmpeg zip libzip-dev && \
    docker-php-ext-configure zip && \
    docker-php-ext-install zip && \
    # Install composer
    php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer && \
    # Install php modules
    apt-get install -y libpq-dev && \
    docker-php-ext-install pdo_pgsql && \
    # Install nodejs
    curl -sL https://deb.nodesource.com/setup_15.x | bash - && \
    apt-get install -y nodejs && \
    # Cleanup
    apt-get clean && \
    # Use the default development configuration
    mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini" && \
    # Patch php configuration files
    sed -i "s/^upload_max_filesize\s=.*/upload_max_filesize = ${MAX_UPLOAD_FILESIZE}M/" $PHP_INI_DIR/php.ini && \
    sed -i "s/^post_max_size\s=.*/post_max_size = ${MAX_UPLOAD_FILESIZE}M/" $PHP_INI_DIR/php.ini && \
    sed -i "s/^pgsql\.auto_reset_persistent\s=.*/pgsql.auto_reset_persistent = On/" $PHP_INI_DIR/php.ini && \
    sed -i "s/^pgsql\.max_persistent\s=.*/pgsql.max_persistent = 10/" $PHP_INI_DIR/php.ini && \
    sed -i "s/^variables_order\s=.*/variables_order = \"EGPCS\"/" $PHP_INI_DIR/php.ini && \
    # Create directories
    mkdir -p /volume/temp && chown $USER /volume/temp && \
    mkdir -p /volume/media && chown $USER /volume/media && \
    mkdir -p /code && chown $USER /code && \
    mkdir -p /home && chown $USER /home

USER $USER

ENV HOME=/home

WORKDIR /code
