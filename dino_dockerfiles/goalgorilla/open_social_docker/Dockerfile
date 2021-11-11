FROM drupal:8.9
MAINTAINER devel@goalgorilla.com

# Install packages.
RUN apt-get update && apt-get install -y \
  zlib1g-dev \
  mariadb-client \
  git \
  msmtp \
  libzip-dev \
  nano \
  vim && \
  apt-get clean

ADD mailcatcher-msmtp.conf /etc/msmtprc

RUN echo 'sendmail_path = "/usr/bin/msmtp -t"' > /usr/local/etc/php/conf.d/mail.ini

ADD php.ini /usr/local/etc/php/php.ini

# Install extensions
RUN docker-php-ext-install zip bcmath exif

# Install Composer.
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Install Open Social via composer.
RUN rm -f /var/www/composer.lock
RUN rm -rf /root/.composer

ADD composer.json /var/www/composer.json
WORKDIR /var/www/
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN COMPOSER_MEMORY_LIMIT=-1 composer install --prefer-dist --no-interaction --no-dev

WORKDIR /var/www/html/
RUN chown -R www-data:www-data *

# Unfortunately, adding the composer vendor dir to the PATH doesn't seem to work. So:
RUN ln -s /var/www/vendor/bin/drush /usr/local/bin/drush

RUN php -r 'opcache_reset();'

# Fix shell.
RUN echo "export TERM=xterm" >> ~/.bashrc
