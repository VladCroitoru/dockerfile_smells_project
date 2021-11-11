# Docker - Customer Portal Drupal - API Behat tests
#
# VERSION       dev
# Behat docker image for Drupal Customer Portal API
#FROM itapregistry.a1.vary.redhat.com/rhel7-platops-php55
#FROM reg.paas.redhat.com/rhel7-platops-php55
FROM php:7.0
MAINTAINER Dan Kolbas <dkolbas@redhat.com>

# Install necessary extensions for PHP.
RUN apt-get update && apt-get install -y apt-utils zlib1g-dev libmcrypt-dev libpq-dev libxml2 libxml2-dev openssl git

# Install PHP extensions.
RUN docker-php-ext-install zip

# Install composer.
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
 && php composer-setup.php --install-dir=/usr/bin --filename=composer \
 && php -r "unlink('composer-setup.php');"

# Add composer bin path.
ENV PATH /root/.composer/vendor/bin:$PATH

# Create target folder.
RUN mkdir -p /opt/cpdrupal-api-behat

# Copy the source code to the container.
COPY . /opt/cpdrupal-api-behat/

WORKDIR /opt/cpdrupal-api-behat/
RUN composer install

RUN sed -i "s,;date.timezone =,date.timezone = \'America/New_York\'," /usr/local/include/php/main/php_ini.h

