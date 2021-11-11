FROM php:7.1.16
MAINTAINER Chris Kankiewicz <ckankiewicz@freedomdebtrelief.com>

# Install dependencies
RUN apt-get update && apt-get install -y jq libmemcached-dev libyaml-dev python unzip zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install PHP extensions
RUN docker-php-ext-install pdo pdo_mysql \
    && pecl install memcached && docker-php-ext-enable memcached \
    && pecl install yaml && docker-php-ext-enable yaml \
    && pecl install xdebug && docker-php-ext-enable xdebug

# Create php.ini
COPY files/php.ini /usr/local/etc/php/php.ini

# Install Google Cloud SDK
RUN mkdir --parents --verbose /opt/google-cloud-sdk
RUN curl --silent https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-185.0.0-linux-x86_64.tar.gz \
    | tar -xzv --strip-components=1 -C /opt/google-cloud-sdk \
    && ln -s /opt/google-cloud-sdk/bin/gcloud /usr/local/bin/gcloud
