FROM php:7.0.22-apache

ENV APACHE_DOCUMENT_ROOT /var/www/html/public

RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# Install dependencies required by php-extensions
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl git zip \
  libc-client-dev libkrb5-dev libpng-dev libmcrypt-dev mysql-client libmagickwand-dev \
  mysqltuner libmemcached-dev libicu-dev

# Install composer and the php-extensions themselves.
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
  docker-php-ext-install gd mcrypt pdo_mysql zip intl && \
  docker-php-ext-configure imap --with-kerberos --with-imap-ssl && docker-php-ext-install imap && \
  echo '' | pecl install redis && docker-php-ext-enable redis && \
  echo '' | pecl install imagick && docker-php-ext-enable imagick && \
  echo '' | pecl install memcached && docker-php-ext-enable memcached

RUN a2enmod rewrite headers

ADD ./src/install.sh /install.sh
RUN chmod +x /install.sh

ADD ./src/php.ini /usr/local/etc/php/php.ini

CMD ["/install.sh"]
