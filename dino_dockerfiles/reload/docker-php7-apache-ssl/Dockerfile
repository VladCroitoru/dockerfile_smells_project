FROM composer:1.10.22 AS composer

FROM phusion/baseimage:0.11

COPY --from=composer /usr/bin/composer /usr/bin/composer

COPY files/etc/ /etc/
# Add our tools to PATH.
COPY files/bin /usr/local/bin/

ENV PATH /root/.composer/vendor/bin:$PATH
ENV PHP_VERSION 7.0

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN \
  # Add a repo that contains php ${PHP_VERSION}
  LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \
  # Do the remaining installation of packages.
  install_clean \
      apache2 \
      # Drush needs this to work
      mysql-client \
      libapache2-mod-php${PHP_VERSION} \
      # Default extensions.
      php${PHP_VERSION}-curl \
      php${PHP_VERSION}-gd \
      php${PHP_VERSION}-mysql \
      php${PHP_VERSION}-xml \
      php${PHP_VERSION}-xdebug \
      php${PHP_VERSION}-mbstring \
      php${PHP_VERSION}-mcrypt \
      php${PHP_VERSION}-soap \
      # Added for installing composer.
      php${PHP_VERSION}-zip \
      # Other extensions
      php${PHP_VERSION}-intl \
      php-memcache \
      php-memcached \
      # For default snakeoil certificates which SSL is configuered to use
      # per default in Apache.
      ssl-cert \
      dnsutils \
      imagemagick \
      unzip \
  && \
  a2enmod rewrite && \
  a2enmod ssl && \
  a2ensite default-ssl && \
  a2enconf drupal && \
  phpenmod drupal-recommended && \
  phpdismod xdebug && \
  # Drush 8 is the current stable that supports Drupal version 6, 7 and 8.
  composer global require drush/drush:8.*

ENV PHP_DEFAULT_EXTENSIONS calendar ctype curl dom exif fileinfo ftp gd gettext iconv json mcrypt mysql mysqli mysqlnd opcache pdo pdo_mysql phar posix readline shmop simplexml soap sockets sysvmsg sysvsem sysvshm tokenizer wddx xml xmlreader xmlwriter xsl mbstring zip

EXPOSE 80 443
WORKDIR /var/www/html
