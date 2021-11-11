FROM php:5-apache

RUN apt-get update && apt-get install -y \
    php5-mysql \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
  --no-install-recommends && rm -r /var/lib/apt/lists/* \
  && docker-php-ext-install mysql mysqli pdo pdo_mysql opcache mbstring \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install gd \
  && a2enmod rewrite
  
# Install Drush and Drupal Console.
RUN apt-get update && apt-get install -y \
    mysql-client \
  --no-install-recommends && rm -r /var/lib/apt/lists/* \
  && php -r "readfile('https://s3.amazonaws.com/files.drush.org/drush.phar');" > /usr/local/bin/drush \
  && chmod +x /usr/local/bin/drush \
  && curl https://drupalconsole.com/installer -L -o drupal.phar \
  && mv drupal.phar /usr/local/bin/drupal \
  && chmod +x /usr/local/bin/drupal
  
# Use our own php config file
COPY config/php.ini /usr/local/etc/php/

# Copy Drupal into the webroot
COPY src/ /var/www/html/

VOLUME ["/var/www/html"]

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["apache2-foreground"]
