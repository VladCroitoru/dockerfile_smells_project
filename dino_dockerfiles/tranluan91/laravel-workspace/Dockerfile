FROM ubuntu:16.04

MAINTAINER Tran Duc Thang <thangtd90@gmail.com>

RUN DEBIAN_FRONTEND=noninteractive
RUN locale-gen en_US.UTF-8

ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LC_CTYPE=UTF-8
ENV LANG=en_US.UTF-8
ENV TERM xterm

# Install "software-properties-common" (for the "add-apt-repository")
RUN apt-get update && apt-get install -y \
    software-properties-common

# Add the "PHP 7" ppa
RUN add-apt-repository -y \
    ppa:ondrej/php

# Install PHP-CLI 7, some PHP extentions and some useful Tools with APT
RUN apt-get update && apt-get install -y --force-yes \
        php7.1-cli \
        php7.1-common \
        php7.1-curl \
        php7.1-json \
        php7.1-xml \
        php7.1-mbstring \
        php7.1-mcrypt \
        php7.1-mysql \
        php7.1-pgsql \
        php7.1-sqlite \
        php7.1-sqlite3 \
        php7.1-zip \
        php7.1-memcached \
        php7.1-gd \
        php7.1-fpm \
        php7.1-xdebug \
        php7.1-dev \
        libcurl4-openssl-dev \
        libedit-dev \
        libssl-dev \
        libxml2-dev \
        xz-utils \
        sqlite3 \
        libsqlite3-dev \
        git \
        curl \
        vim \
        nano \
        net-tools \
        pkg-config \
        iputils-ping

# remove load xdebug extension (only load on phpunit command)
RUN sed -i 's/^/;/g' /etc/php/7.1/cli/conf.d/20-xdebug.ini

# Add bin folder of composer to PATH.
RUN echo "export PATH=${PATH}:/var/www/laravel/vendor/bin:/root/.composer/vendor/bin" >> ~/.bashrc

# Load xdebug Zend extension with phpunit command
RUN echo "alias phpunit='php -dzend_extension=xdebug.so /var/www/laravel/vendor/bin/phpunit'" >> ~/.bashrc

# Install mongodb extension
RUN pecl channel-update pecl.php.net && pecl install mongodb-1.1.9
RUN echo "extension=mongodb.so" >> /etc/php/7.1/cli/conf.d/20-mongodb.ini

# Install Nodejs
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g gulp-cli bower eslint babel-eslint eslint-plugin-react yarn

# Install SASS
RUN apt-get install -y ruby \
    && gem install sass

# Install Compass
RUN apt-get install -y ruby-dev
RUN gem install --no-rdoc --no-ri compass

# Install Composer, PHPCS and Framgia Coding Standard,
# PHPMetrics, PHPDepend, PHPMessDetector, PHPCopyPasteDetector
RUN curl -s http://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && composer global require 'squizlabs/php_codesniffer' \
        'phpmetrics/phpmetrics' \
        'pdepend/pdepend' \
        'phpmd/phpmd' \
        'sebastian/phpcpd' \
    && cd ~/.composer/vendor/squizlabs/php_codesniffer/CodeSniffer/Standards \
    && git clone https://github.com/wataridori/framgia-php-codesniffer.git Framgia

# Create symlink
RUN ln -s /root/.composer/vendor/bin/phpcs /usr/bin/phpcs \
    && ln -s /root/.composer/vendor/bin/pdepend /usr/bin/pdepend \
    && ln -s /root/.composer/vendor/bin/phpmetrics /usr/bin/phpmetrics \
    && ln -s /root/.composer/vendor/bin/phpmd /usr/bin/phpmd \
    && ln -s /root/.composer/vendor/bin/phpcpd /usr/bin/phpcpd

# Install framgia-ci-tool
RUN curl -o /usr/bin/framgia-ci https://raw.githubusercontent.com/framgia/ci-report-tool/master/dist/framgia-ci \
    && chmod +x /usr/bin/framgia-ci

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /var/www/laravel
