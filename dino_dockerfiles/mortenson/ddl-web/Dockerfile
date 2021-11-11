FROM php:7.1-apache
# Customize container to match Drupal 8 requirements
RUN a2enmod rewrite
RUN apt-get update -y \
 && apt-get install -y libpng-dev zip unzip mysql-client ssmtp mailutils libfreetype6-dev libjpeg62-turbo-dev libfontconfig \
 && rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd opcache pdo pdo_mysql zip bcmath exif
RUN pecl install apcu && echo extension=apcu.so > /usr/local/etc/php/conf.d/docker-php-ext-apcu.ini
# Install XDebug
RUN pecl install xdebug && docker-php-ext-enable xdebug
# Configure sendmail
RUN echo "hostname=localhost.localdomain" > /etc/ssmtp/ssmtp.conf
RUN echo "mailhub=mailhog:1025" >> /etc/ssmtp/ssmtp.conf
# Install Drush Launcher
RUN curl -OL https://github.com/drush-ops/drush-launcher/releases/download/0.6.0/drush.phar && \
  chmod +x drush.phar && \
  mv drush.phar /usr/local/bin/drush
# Install a fallbck version of Drush
RUN curl -OL https://github.com/drush-ops/drush/releases/download/8.1.17/drush.phar && \
  chmod +x drush.phar && \
  mv drush.phar /usr/local/bin/drush8
# Install Drupal Console Launcher
RUN curl https://drupalconsole.com/installer -L -o drupal.phar && \
  chmod +x drupal.phar && \
  mv drupal.phar /usr/local/bin/drupal
# Install PhantomJS
RUN mkdir /tmp/phantomjs && \
  curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
  | tar -xj --strip-components=1 -C /tmp/phantomjs && \
  mv /tmp/phantomjs/bin/phantomjs /usr/local/bin
# Add our custom configuration
COPY php.ini /usr/local/etc/php/
COPY apache2.conf /etc/apache2/custom.conf
RUN echo "Include custom.conf" >> /etc/apache2/apache2.conf
# Use a custom docroot
ENV APACHE_DOCUMENT_ROOT /var/www/html/docroot
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf
