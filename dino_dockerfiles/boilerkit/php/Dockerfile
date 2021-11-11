# https://github.com/docker-library/php/blob/master/7.2/alpine3.7/fpm/Dockerfile
FROM php:7.2-fpm-alpine3.7

ENV PHPIZE_DEPS $PHPIZE_DEPS

RUN apk add --no-cache --update --virtual .phpize-deps $PHPIZE_DEPS \
    freetype-dev \
    libpng-dev \
    libtool \
    libxml2-dev \
    postgresql-dev \
    \
    && apk add --no-cache --update \
      gmp-dev \
      icu-dev \
      imagemagick-dev \
      imap-dev \
      libjpeg-turbo-dev \
      libzip-dev \
    \
    && apk add --no-cache --update \
      git \
      hiredis \
      postgresql \
      shadow \
      wget \
      zsh \
    \
    && docker-php-ext-configure gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    \
    && docker-php-ext-install intl \
    \
    && docker-php-ext-install soap \
    \
    && docker-php-ext-install bcmath \
    \
    && docker-php-ext-install gmp \
    \
    && docker-php-ext-configure imap --with-imap --with-imap-ssl \
    && docker-php-ext-install imap \
    \
    && docker-php-ext-configure zip --with-libzip \
    && docker-php-ext-install zip \
    \
    && docker-php-ext-install pdo_pgsql \
    \
    && pecl install imagick-3.4.3 \
    && docker-php-ext-enable imagick \
    \
    && pecl install redis \
    && docker-php-ext-enable redis \
    \
    && pecl install xdebug \
    && docker-php-ext-enable xdebug \
    \
    && apk del .phpize-deps

#
RUN curl -sS "https://getcomposer.org/installer" | php -- --install-dir=/usr/local/bin --filename=composer

#
RUN mkdir /var/www/.composer \
    && chown -R www-data:www-data /var/www/.composer

#
ENV PATH "$PATH:./vendor/bin"

#
COPY conf/php.ini /usr/local/etc/php/

#
RUN chsh --shell /bin/zsh root \
  && chsh --shell /bin/zsh www-data

# 
WORKDIR /app
