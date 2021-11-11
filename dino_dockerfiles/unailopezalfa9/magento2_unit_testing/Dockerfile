FROM ubuntu:16.04
MAINTAINER Unai Lopez <unai.lopez@alfa9.com>

# install OS packages
RUN apt-get update && apt-get install -y \
    git \
    curl \
    nano \
    php \
    php-cli \
    php-curl \
    php-gd \
    php-dom \
    php-intl \
    php-json \
    php-xml \
    php-xsl \
    php-mbstring \
    php-mcrypt \
    php-mysql \
    php-soap \
    php-zip \
    && apt-get clean
    
# Install extra utils
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && chmod a+x /usr/local/bin/composer \
