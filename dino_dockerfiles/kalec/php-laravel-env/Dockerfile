FROM php:7.3-apache-stretch

LABEL maintainer="Kalegos"

#Install PHP Extensions
RUN docker-php-ext-install pdo_mysql opcache \
	&& pecl install xdebug \
	&& docker-php-ext-enable xdebug \
	&& a2enmod rewrite negotiation

#Install composer
COPY /composer/composer-installer.sh /usr/local/bin/composer-installer
RUN apt-get -yqq update \
	&& apt-get -yqq install --no-install-recommends zip unzip git gnupg nano \
	&& chmod +x /usr/local/bin/composer-installer \
	&& composer-installer \
	&& mv composer.phar /usr/local/bin/composer \
	&& chmod +x /usr/local/bin/composer \
	&& rm /usr/local/bin/composer-installer \
	&& composer --version
	
#Install NodeJs & Gulp
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash - \
	&& apt-get install -yqq nodejs npm yarn \
	&& node --version \
	&& npm --version

RUN npm install --global gulp-cli -g \
	&& npm install --global gulp -D \
	&& gulp --help

COPY /php/php.ini /usr/local/etc/php/
COPY /apache/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY /php/xdebug-dev.ini /usr/local/etc/php/conf.d/xdebug-dev.ini

# Cache Composer dependencies
WORKDIR /tmp
RUN curl -OL https://raw.githubusercontent.com/laravel/laravel/master/composer.json
# ADD composer.json composer.lock /tmp/

RUN mkdir -p database/seeds \
	mkdir -p database/factories \
	&& composer install \
	--no-interaction \
	--no-plugins \
	--no-scripts \
	--prefer-dist \
	&& composer update \
	--no-interaction \
	--no-plugins \
	--no-scripts \
	--prefer-dist \
	&& rm -rf composer.json composer.lock \
	database/ vendor/

