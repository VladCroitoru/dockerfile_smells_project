FROM php:7.1.13-fpm

RUN apt-get update \
  && apt-get install -y \
    libfreetype6-dev \
    libicu-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libxslt1-dev \
    git \
    vim \
    wget \
    lynx \
    psmisc \
    bzip2 \
    cron \
    supervisor \
  && apt-get clean

RUN docker-php-ext-configure \
    gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/; \
  docker-php-ext-install \
    gd \
    intl \
    mbstring \
    mcrypt \
    pdo_mysql \
    xsl \
    zip \
    opcache \
    soap \
    bcmath

RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini
RUN echo "date.timezone=Europe/Warsaw" > $PHP_INI_DIR/conf.d/date_timezone.ini

VOLUME /root/composer

ENV COMPOSER_HOME /root/composer

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
	composer selfupdate

WORKDIR /tmp

RUN curl -sL  https://deb.nodesource.com/setup_7.x | bash - && \
  apt-get install -y nodejs
