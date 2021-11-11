FROM php:8.0.3-apache

RUN apt-get -qq update \
        && apt-get install --assume-yes --quiet --no-install-recommends \
            ca-certificates git curl libpng-dev libfreetype6-dev libjpeg62-turbo-dev \
            libicu-dev libxml++2.6-dev unzip libzip-dev libpq5 libpq-dev vim default-mysql-client \
    && docker-php-ext-configure gd --with-freetype=/usr/include/ --with-jpeg=/usr/include/ > /dev/null \
    && docker-php-ext-install bcmath  exif gd intl pdo_mysql pdo_pgsql pgsql soap zip xml mysqli \
    && docker-php-ext-enable opcache \
    && docker-php-source delete > /dev/null \
# remove dev-dependencies
    && apt-get remove --assume-yes --quiet libpng-dev libfreetype6-dev libpq-dev libjpeg62-turbo-dev libicu-dev libxml++2.6-dev libzip-dev python3 \
    && rm -r /var/lib/apt/lists/*

# Configure time
RUN rm /etc/localtime \
    && ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime \
# Install composer
    && curl -sS https://getcomposer.org/installer | \
        php -- --install-dir=/usr/bin/ --filename=composer \
# Configure apache mods
    && ln -s /etc/apache2/mods-available/expires.load /etc/apache2/mods-enabled/ \
    && ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled/ \
    && ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/ \
# Setup user/group
    && groupadd -g 1000 appuser  \
    && useradd -r -u 1000 -g appuser appuser

COPY vhost.conf /etc/apache2/sites-available/000-default.conf
COPY php.ini /usr/local/etc/php
RUN sed -i "s/80/8000/g" /etc/apache2/ports.conf \
    && mkdir -p /var/run/apache2 \
    && chown -R appuser: /var/run/apache2/ \
    && chown -R appuser: /var/www \
    && chown -R appuser: /var/log/apache2
EXPOSE 8000

ENV APACHE_RUN_USER=appuser
WORKDIR "/var/www"
CMD ["apache2-foreground"]
