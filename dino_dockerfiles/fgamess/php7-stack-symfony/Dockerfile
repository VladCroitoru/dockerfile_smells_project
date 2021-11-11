FROM php:7.1-fpm

ENV DEBIAN_FRONTEND noninteractive
ENV DEFAULT_TIMEZONE Asia/Dubai

### Install dependencies
RUN apt-get update \
    && apt-get install -y \
    locales tzdata \
    git \
    zlib1g-dev \
    libmcrypt-dev \
    openssh-server \
    libicu-dev \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libpq-dev \
    libxml2-dev \
    zip \
    unzip \
    --no-install-recommends \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-install bcmath \
    mbstring \
    opcache \
    pcntl \
    zip \
    mcrypt \
    pdo \
    pdo_mysql \
    pdo_pgsql \
    mysqli \
    exif \
    intl \
    soap

RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install pdo pdo_pgsql pgsql

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd


#Add composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer --version

# Set timezone
RUN mkdir /tz && mv /etc/timezone /tz/ && mv /etc/localtime /tz/ \
    && ln -s /tz/timezone /etc/ && ln -s /tz/localtime /etc/

#  Common for all tradetracker images
RUN echo "${DEFAULT_TIMEZONE}" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata \
    && cp /etc/timezone /tz/ && cp /etc/localtime /tz/ &2> \dev\null

VOLUME /tz

# install xdebug
RUN pecl install xdebug
RUN docker-php-ext-enable xdebug
RUN echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.cli_color=1\nxdebug.remote_autostart=1\nxdebug.remote_connect_back=1" > /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN docker-php-ext-enable xdebug

RUN usermod -u 1000 www-data

RUN echo 'alias sf="php bin/console"' >> ~/.bashrc

WORKDIR /var/www
