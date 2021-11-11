FROM php:5-apache
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        php5-cli \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install mysql mysqli pdo pdo_mysql

RUN a2enmod rewrite

RUN curl -SL https://github.com/textpattern/textpattern/tarball/4.5.7 > textpattern.tar.gz
RUN tar -xzf textpattern.tar.gz -C /var/www/html --strip-components=1
RUN	chmod 755 -R /var/www/html && \
	chown www-data: -R /var/www/html
