FROM php:7.0-apache-jessie
MAINTAINER Virgilio Missão Neto <virgilio.missao.neto@gmail.com>

RUN apt-get update \
  && apt-get install -y \
  libpq-dev \
  libfreetype6-dev \
  libjpeg62-turbo-dev \
  libmcrypt-dev \
  libpng12-dev \
  zlib1g-dev \
  libicu-dev \
  libxml2-dev \
  libmemcached-dev \
  libssl-dev \
  curl \
  git-core \
  ruby \
  g++

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-configure intl \
  && docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
  && docker-php-ext-install -j$(nproc) mbstring xml iconv mcrypt gd intl xmlrpc zip bcmath sockets pdo pdo_mysql zip pcntl soap

RUN curl https://phar.phpunit.de/phpunit.phar -L > phpunit.phar \
  && chmod +x phpunit.phar \
  && mv phpunit.phar /usr/local/bin/phpuni

RUN pecl install -o -f mongodb xdebug-2.5.5

RUN docker-php-ext-enable mongodb xdebug

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash \
  && bash -i -c 'nvm install node' && bash -i -c 'nvm use node' \
  && bash -i -c 'npm install bower gulp -g'

COPY default-vhost.conf /etc/apache2/sites-available/default.conf
RUN a2dissite 000-default.conf && a2ensite default.conf && a2enmod rewrite

COPY php.ini.development /usr/local/etc/php/php.ini

RUN usermod -u 1000 www-data && groupmod -g 1000 www-data
