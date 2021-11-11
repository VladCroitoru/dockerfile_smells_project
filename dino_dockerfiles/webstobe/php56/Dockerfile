FROM composer AS composer
FROM php:5.6-apache
# 02
MAINTAINER Nando Bosshart <nando@webstobe.ch>
#03 set ENV variables
ENV APACHE_DOCUMENT_ROOT="/var/www/web" COMPOSER_ALLOW_SUPERUSER=1 PATH="/var/www/vendor/bin:$PATH"

# 04 set desired timezone
RUN echo Europe/Zurich >/etc/timezone && \
dpkg-reconfigure -f noninteractive tzdata
# 05
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf && \
    sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# 06 install some additions on top of our image
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        nano \
        vim \
        git \
        unzip \
        zip \
        ssh \
        libxml2-dev libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        rsync \
        zlib1g-dev \
        graphicsmagick \
        mysql-client && \
# configure extensions
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install -j$(nproc) mysqli soap gd zip opcache && \
    apt-get clean && \
    apt-get -y purge \
        libxml2-dev libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        zlib1g-dev && \
    rm -rf /var/lib/apt/lists/* /usr/src/*
# 07 configure Apache
RUN a2enmod rewrite ssl proxy proxy_http

# 08 install composer globally - the ENV variables are already set:
COPY --from=composer /usr/bin/composer /usr/bin/composer

# 09 Configure volumes
# these volumes stay persistent:
VOLUME /var/www

# lets try this for windows:
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["apache2-foreground"]
