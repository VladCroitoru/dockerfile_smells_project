FROM php:7-apache

ARG COMPOSER_ALLOW_SUPERUSER=1

RUN apt-get update && apt-get install -y unzip libicu-dev vim \
	&& docker-php-ext-install intl \
	&& a2enmod rewrite

# Install and configure Composer and Symfony skeleton
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
	&& composer create-project symfony/skeleton /var/www/kyjoukan 3.4

WORKDIR "/var/www/kyjoukan"

# Install Kyjoukan into Symfony
COPY . src/Kyjoukan
RUN ln -s ../components public/components \
	&& cp src/Kyjoukan/Resources/public/favicon.ico public/favicon.ico \
	&& cp src/Kyjoukan/docker/config/kyjoukan.conf /etc/apache2/sites-enabled/000-default.conf \
	&& cp src/Kyjoukan/docker/config/routes.yaml config/routes.yaml \
	&& cp src/Kyjoukan/docker/config/services.yaml config/services.yaml \
	&& cp src/Kyjoukan/docker/config/doctrine.yaml config/packages/doctrine.yaml \
	&& composer config repositories.kyjoukan path /var/www/kyjoukan/src/Kyjoukan \
	&& composer config extra.symfony.allow-contrib true \
	&& composer require translation annotations \
		orm form validator templating monolog asset assetic-bundle stof/doctrine-extensions-bundle \
		profiler \
		abienvenu/kyjoukan:@dev

# Create database and load example data
RUN bin/console assetic:dump \
	&& bin/console assets:install \
	&& mkdir data \
	&& bin/console doctrine:schema:create \
	&& bin/console doctrine:fixtures:load --append \
	&& chown -R www-data.www-data data \
	&& chown -R www-data.www-data var/cache \
	&& chown -R www-data.www-data var/log
