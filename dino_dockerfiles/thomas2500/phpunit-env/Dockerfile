FROM php:latest
MAINTAINER Thomas Bella <thomas+docker@bella.network>

# Install additional packages
RUN apt-get update && apt-get install -y ca-certificates git gettext openssh-client unzip wget curl build-essential php-pear

# Install php extensions
RUN docker-php-ext-install bcmath
RUN apt-get install libbz2-dev -yqq && docker-php-ext-install bz2
RUN apt-get install libcurl3-dev -yqq && docker-php-ext-install curl
RUN docker-php-ext-install exif
RUN docker-php-ext-install fileinfo
RUN apt-get install -yqq libssl-dev && docker-php-ext-install ftp
RUN apt-get install -yqq libfreetype6-dev libjpeg62-turbo-dev libpng12-dev && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && docker-php-ext-install gd
RUN apt-get install libmhash2 libmhash-dev -yqq && docker-php-ext-install hash
RUN apt-get install libssl-dev libc-client2007e-dev libkrb5-dev -yqq && docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos && docker-php-ext-install imap
RUN apt-get install zlib1g-dev libicu-dev g++ -yqq && docker-php-ext-install intl
RUN docker-php-ext-install json
RUN docker-php-ext-install mbstring
RUN apt-get install libmcrypt4 libmcrypt-dev -yqq && docker-php-ext-install mcrypt
RUN docker-php-ext-install opcache
RUN docker-php-ext-install pdo_mysql
RUN apt-get install -y libpq-dev && docker-php-ext-install pdo_pgsql
RUN apt-get install libsqlite0 sqlite sqlite3 libsqlite3-dev -yqq && docker-php-ext-install pdo_sqlite
RUN docker-php-ext-install session
RUN apt-get install zlib1g-dev -yqq && docker-php-ext-install zip
RUN apt-get install libxml2-dev -yqq && docker-php-ext-install simplexml xmlrpc xml

# Cleanup
RUN apt-get clean && rm -r /var/lib/apt/lists/*

# Install redis
RUN pecl install redis && docker-php-ext-enable redis

# Install php-apcu
RUN pecl install apcu
RUN echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini

# Install xdebug
RUN pecl install xdebug && docker-php-ext-enable xdebug

# Set timezone to Vienna
RUN touch /usr/local/etc/php/conf.d/timezone.ini && echo "date.timezone = UTC" > /usr/local/etc/php/conf.d/timezone.ini

# Install composer and put binary into $PATH
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/ \
    && ln -s /usr/local/bin/composer.phar /usr/local/bin/composer

# Install phpunit and put binary into $PATH
RUN wget -O /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar \
    && chmod 755 /usr/local/bin/phpunit \
    && chmod +x /usr/local/bin/phpunit

VOLUME ["/app"]
WORKDIR /app

CMD ["phpunit"]
