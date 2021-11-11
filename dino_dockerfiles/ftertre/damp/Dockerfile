FROM php:5.6-apache
RUN apt-get update && apt-get install -y \
    locales \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmcrypt-dev \
    libpng12-dev \
		libpq-dev \
	&& docker-php-ext-install -j$(nproc) iconv mcrypt \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) gd \
  && docker-php-ext-install -j$(nproc) pdo_mysql \
	&& docker-php-ext-install -j$(nproc) pdo_pgsql \
	&& docker-php-ext-install -j$(nproc) gettext \
	&& docker-php-ext-install -j$(nproc) exif \
	&& cp /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/
