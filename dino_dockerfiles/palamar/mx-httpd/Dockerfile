FROM php:5.6-apache
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y g++
RUN apt-get install -y libmcrypt-dev libreadline-dev \
    && docker-php-ext-install -j$(nproc) mcrypt
RUN docker-php-ext-install -j$(nproc) bcmath
RUN apt-get install -y libicu-dev \
    && docker-php-ext-install -j$(nproc) intl
RUN docker-php-ext-install -j$(nproc) mbstring
RUN docker-php-ext-install -j$(nproc) mcrypt
RUN docker-php-ext-install -j$(nproc) hash
RUN apt-get install -y \
		libxml2-dev \
		libxslt-dev \
    && docker-php-ext-install -j$(nproc) simplexml
RUN docker-php-ext-install -j$(nproc) xml
RUN docker-php-ext-install -j$(nproc) xsl
RUN docker-php-ext-install -j$(nproc) soap
RUN docker-php-ext-install -j$(nproc) json
RUN docker-php-ext-install -j$(nproc) dom
RUN apt-get install -y zlib1g-dev \
    && docker-php-ext-install -j$(nproc) zip
RUN docker-php-ext-install -j$(nproc) pdo
RUN apt-get install -y libpq-dev \
    && docker-php-ext-install -j$(nproc) pdo_pgsql
RUN docker-php-ext-install -j$(nproc) pdo_mysql
RUN docker-php-ext-install -j$(nproc) gettext
RUN apt-get install -y libbz2-dev \
    && docker-php-ext-install -j$(nproc) bz2
RUN docker-php-ext-install -j$(nproc) iconv
RUN apt-get install -y libcurl3-dev \
    && docker-php-ext-install -j$(nproc) curl
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install opcache
RUN pecl install xdebug
RUN a2enmod rewrite
COPY conf.d/www.conf /etc/apache2/conf-enabled/
COPY sites-enabled/m1.conf /etc/apache2/sites-enabled/
WORKDIR /www/
EXPOSE 80
