FROM php:5.5-apache
# based on debian:jessie
# https://github.com/docker-library/php/blob/master/5.5/apache/Dockerfile

ENV TYPO3_VERSION 6.2.10

# Download requirements
RUN apt-get update -qq && \
    apt-get install -qq -y --no-install-recommends \
        wget \
        unzip \
        re2c \
        file \
        mysql-client \
        imagemagick \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libxml2-dev

# Cleanup apt/dpkg
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Download + extract TYPO3 source, set permissions
RUN cd /var/www && \
    wget -qO - http://prdownloads.sourceforge.net/typo3/typo3_src-${TYPO3_VERSION}.tar.gz \
    | tar zxf - && \
    cd html && \
    ln -s ../typo3_src-${TYPO3_VERSION} typo3_src && \
    ln -s typo3_src/index.php index.php && \
    ln -s typo3_src/typo3 typo3 && \
    touch FIRST_INSTALL && \
    chown -R www-data:www-data /var/www

# PHP configuration for TYPO3
COPY config/php.ini /usr/local/etc/php/php.ini

# PHP extensions
RUN docker-php-ext-install mysqli soap zip mcrypt iconv opcache > /dev/null && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install gd

EXPOSE 80
