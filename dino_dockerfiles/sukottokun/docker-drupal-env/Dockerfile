FROM debian

RUN apt-get update && apt-get install -y \
	build-essential \
	curl \
	git \
	gcc \
	make \
	php5-cli \
	php5-dev \
	php5-mysql \
	php-pear \
	php5-curl \
	php5-mcrypt \
	php5-gd \
	php5-json \
	php5-xdebug \
	nginx

RUN php5enmod mcrypt

# Setup composer
RUN curl -sS https://getcomposer.org/installer | php \
	&& mv composer.phar /usr/local/bin/composer
ENV PATH $PATH:/root/.composer/vendor/bin

# Setup phpunit
RUN curl -sS https://phar.phpunit.de/phpunit.phar > phpunit.phar \
	&& chmod +x phpunit.phar \
	&& mv phpunit.phar /usr/local/bin/phpunit

# Setup drush (dev-master for Drupal 8)
RUN composer global require drush/drush:~8 && composer global update

# Fix for Drupal
RUN echo "xdebug.max_nesting_level=256" >> /etc/php5/cli/conf.d/20-xdebug.ini

EXPOSE 80
