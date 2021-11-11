# See https://github.com/docker-library/php/blob/173945670390f6595da8f93ae46b442167ff05be/5.6/fpm/Dockerfile
FROM php:7-cli

MAINTAINER McMakler <admin@mcmakler.de>

RUN apt-get update \
&& apt-get install -y imagemagick libmagickwand-dev libmagickcore-dev \
&& apt-get install -y libmcrypt-dev libcurl4-gnutls-dev libicu-dev libxslt-dev libssl-dev

RUN docker-php-ext-install -j$(nproc) iconv mcrypt mysqli pdo_mysql gd zip curl bcmath opcache mbstring \
&& docker-php-ext-install -j$(nproc) curl json intl session xmlrpc xsl \
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
&& docker-php-ext-install -j$(nproc) gd \
&& docker-php-ext-enable iconv mcrypt pdo_mysql gd zip curl bcmath opcache mbstring \
&& docker-php-ext-enable curl json intl session xmlrpc xsl \

RUN pecl install redis \
&& pecl install mongodb \
&& pecl install imagick \
&& docker-php-ext-enable redis mongodb imagick \

RUN apt-get autoremove -y


# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer --version

# Set timezone
RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/UTC /etc/localtime
RUN "date"
