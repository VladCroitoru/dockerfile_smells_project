# Pagekit Docker
# PHP Docker for Pagekit
#
# VERSION 0.2

FROM php:7.1-apache
MAINTAINER Julian Xhokaxhiu <info at julianxhokaxhiu dot com>

LABEL Description="PHP Docker for Pagekit" Vendor="Julian Xhokaxhiu" Version="0.2"

# enable mod_rewrite
RUN a2enmod rewrite

# install the required binaries to be able to build and run Pagekit
RUN apt-get update \
  && curl -sL https://deb.nodesource.com/setup_6.x | bash \
  && apt-get install -y --no-install-recommends libpng12-dev libjpeg-dev libxml2-dev libgraphicsmagick1-dev zlib1g-dev graphicsmagick git zip nodejs \
  && rm -rf /var/lib/apt/lists/* \
  && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
  && docker-php-ext-install gd json mysqli pdo pdo_mysql opcache gettext exif calendar soap sockets wddx zip \
  && curl --silent --show-error https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer \
  && npm install -g bower gulp webpack

# install APCu from PECL
RUN pecl -vvv install apcu && docker-php-ext-enable apcu

# install GMagick from PECL
RUN pecl -vvv install gmagick-beta && docker-php-ext-enable gmagick

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
    echo 'opcache.memory_consumption=128'; \
    echo 'opcache.interned_strings_buffer=8'; \
    echo 'opcache.max_accelerated_files=4000'; \
    echo 'opcache.revalidate_freq=60'; \
    echo 'opcache.fast_shutdown=1'; \
    echo 'opcache.enable_cli=1'; \
  } > /usr/local/etc/php/conf.d/opcache-recommended.ini

# increase upload size
# see http://php.net/manual/en/ini.core.php
RUN { \
    echo "upload_max_filesize = 25M"; \
    echo "post_max_size = 50M"; \
  } > /usr/local/etc/php/conf.d/uploads.ini

# Iron the security of the Docker
RUN { \
    echo "ServerSignature Off"; \
    echo "ServerTokens Prod"; \
    echo "TraceEnable off"; \
  } >> /etc/apache2/apache2.conf

VOLUME /var/www/html