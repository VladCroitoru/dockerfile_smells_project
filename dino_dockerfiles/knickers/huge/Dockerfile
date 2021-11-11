FROM php:5.6-apache

RUN a2enmod rewrite

RUN apt-get update && apt-get install --no-install-recommends -y \
		libpng12-dev libjpeg-dev php5-curl php5-gd openssl \
	&& rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd pdo pdo_mysql zip

RUN curl -s https://getcomposer.org/installer | php \
	&& mv composer.phar /usr/local/bin/composer

WORKDIR /var/www/html

ENV HUGE_VERSION 3.1

RUN set -x \
	&& curl -L https://github.com/panique/huge/archive/v$HUGE_VERSION.tar.gz \
		-o $HUGE_VERSION.tar.gz \
	&& tar -zxf $HUGE_VERSION.tar.gz \
	&& mv -f huge-$HUGE_VERSION/* huge-$HUGE_VERSION/.htaccess . \
	&& composer install \
	&& chmod 0755 -R public/avatars \
	&& rm -rf $HUGE_VERSION.tar.gz huge-$HUGE_VERSION CHANGELOG.md \
		composer.json README.md travis-ci-apache _one-click-installation \
		application/_installation index.html

#RUN set -x \
#	&& apt-get update && apt-get install --no-install-recommends -y git \
#	&& git clone https://github.com/panique/huge . \
#	&& git checkout tags/v$HUGE_VERSION \
#	&& composer install \
#	&& chmod 0755 -R public/avatars \
#	&& apt-get purge --auto-remove -y git \
#	&& rm -rf /var/lib/apt/lists/* .git index.html \
#		.scrutinizer.yml .travis.yml CHANGELOG.md composer.json README.md \
#		travis-ci-apache _one-click-installation application/_installation
