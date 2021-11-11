FROM php:7.0-fpm
MAINTAINER memed <gabriel.couto@memed.com.br>

# Adding sources
RUN echo 'deb http://httpredir.debian.org/debian jessie contrib' >> /etc/apt/sources.list

# Installing packages
RUN apt-get update && apt-get upgrade -y
RUN export DEBIAN_FRONTEND=noninteractive && apt-get install -y --force-yes xorg libssl-dev libxrender-dev fontconfig xfonts-75dpi curl mysql-client libcurl4-gnutls-dev libxml2-dev libpng-dev libicu-dev libmcrypt-dev libjpeg62-turbo-dev libfreetype6-dev libjpeg62-turbo zlib1g-dev libmemcached11 libmemcached-dev git libgmp-dev psmisc xpdf libmagickwand-dev imagemagick xfonts-utils cabextract wget gnupg supervisor nginx

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh && bash nodesource_setup.sh && apt-get -y --force-yes install nodejs

# Install ttf-mscorefonts using DEB
RUN wget http://ftp.us.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-mscorefonts-installer_3.6_all.deb && dpkg -i ttf-mscorefonts-installer_3.6_all.deb && rm -f ttf-mscorefonts-installer_3.6_all.deb

# Building memcached extension
RUN git clone -b php7 https://github.com/php-memcached-dev/php-memcached.git && cd php-memcached && phpize && ./configure && make install

# Creating symlink for libgmb
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h 

# Install PHP Imagick extension
RUN yes "" | pecl install imagick

# Adding PHP extensions
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install pdo curl gd intl pdo_mysql mcrypt dom mbstring gmp bcmath zip opcache
RUN docker-php-ext-enable memcached
RUN docker-php-ext-enable imagick
RUN pecl install mongodb
RUN docker-php-ext-enable mongodb
RUN pecl install timezonedb && \
    docker-php-ext-enable timezonedb

# Cleaning
RUN apt-get clean && apt-get autoremove -y

# Upgrading Node
RUN npm cache clean -f
RUN npm install -g n
RUN n stable

# Adding composer
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-setup.php && php composer-setup.php && php -r "unlink('composer-setup.php');" && mv composer.phar /usr/local/bin/composer

# Adding npm-cache
RUN npm install -g npm-cache

# Adding Grunt
RUN npm install -g grunt-cli

# Adding Bower
RUN npm install -g bower

# Default command
CMD ["php-fpm"]
