FROM sjoerdmulder/teamcity-agent:latest

MAINTAINER Sebastian Nagels <nagels.sebastian@gmail.com>

WORKDIR /tmp

ENV PHPUNIT_VERSION 6.0.7

# Install Dependencies
RUN apt-get update && apt-get install -y software-properties-common

# Add PHP 7.1 Repository
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php

# Install PHP 7.1 + Extensions
RUN apt-get update && apt-get install -y \
	git \
	curl \
	wget \
	php7.1 \
	php7.1-dom \
	php7.1-bcmath \
	php7.1-zip \
	php7.1-mongodb \
	php7.1-bz2 \
	php7.1-curl \
	php7.1-mbstring \
	php7.1-mysqli \
	php7.1-sqlite \
	php7.1-xdebug

# Install Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
	&& php composer-setup.php --install-dir=/usr/bin --filename=composer

# Install PHPUnit
RUN wget https://phar.phpunit.de/phpunit-$PHPUNIT_VERSION.phar \
	&& mv phpunit-$PHPUNIT_VERSION.phar /usr/local/bin/phpunit \
	&& chmod +x /usr/local/bin/phpunit

# Install PHPMD
RUN wget http://static.phpmd.org/php/latest/phpmd.phar \
	&& mv phpmd.phar /usr/local/bin/phpmd \
	&& chmod +x /usr/local/bin/phpmd

# Install PHPCS
RUN wget https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \
	&& mv phpcs.phar /usr/local/bin/phpcs \
	&& chmod +x /usr/local/bin/phpcs

WORKDIR /

