FROM php:7.0-fpm
MAINTAINER Jens Anders Bakke

# -------------------------------------------
# install craft-specific php-modules
# -------------------------------------------

# Imagemagick + PHP 7 is a bit tricky, see https://github.com/docker-library/php/issues/105#issuecomment-196273150
RUN apt-get update \
    && apt-get -y install \
            libmagickwand-dev libmcrypt-dev unzip \
            --no-install-recommends \
    && pecl install imagick \
    && docker-php-ext-enable imagick \
    && rm -r /var/lib/apt/lists/* \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install mcrypt
    
# Install ldap, ref https://github.com/docker-library/php/issues/75
RUN apt-get update && \
    apt-get install libldap2-dev -y && \
    rm -rf /var/lib/apt/lists/* && \
    docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \
    docker-php-ext-install ldap

# No need for composer AFAIK
# RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# download unzip latest craft
RUN ["/bin/bash", "-c", "curl -L -o /craft.zip https://craftcms.com/latest.zip?accept_license=yes"]

# Unzip craft
RUN unzip /craft.zip -d /var/www/

RUN usermod -G staff www-data
RUN chown -R www-data:www-data /var/www

# Copy file source files
COPY public_html /var/www/public_html
COPY craft/plugins /var/www/craft/plugins
COPY craft/templates /var/www/craft/templates
COPY craft/config /var/www/craft/config
RUN chmod 0777 -R /var/www

# Expose everything under /var/www (vendor + html)
# This is required for the nginx setup
VOLUME ["/var/www"]