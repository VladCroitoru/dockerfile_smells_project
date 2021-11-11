FROM php:5.6.31-apache

RUN a2enmod rewrite

RUN apt-get update \
    && apt-get install --no-install-recommends --assume-yes --quiet ca-certificates curl git \
    libfreetype6-dev \
	libjpeg62-turbo-dev \
	libmcrypt-dev \
	libpng-dev \
	libpq-dev \
	libxml2-dev \
    php-soap \
    zlib1g-dev \
    libicu-dev \
    g++ \
    && rm -rf /var/lib/apt/lists/*

RUN curl -Lsf 'https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz' | tar -C '/usr/local' -xvzf -
ENV PATH /usr/local/go/bin:$PATH
RUN go get github.com/mailhog/mhsendmail
RUN cp /root/go/bin/mhsendmail /usr/bin/mhsendmail


RUN docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN pecl install xdebug-2.5.5 \
    && docker-php-ext-enable xdebug

RUN pecl install rar \
    && docker-php-ext-enable rar

RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql

RUN docker-php-ext-configure intl

RUN docker-php-ext-install mysql mysqli pdo pdo_mysql pgsql pdo_pgsql zip sockets soap intl

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php --install-dir=/bin --filename=composer && \
    php -r "unlink('composer-setup.php');"

