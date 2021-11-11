# from https://www.drupal.org/requirements/php#drupalversions
FROM php:5.6-apache

#PREVIOUS MAINTAINER Ian Lintner <ian.lintner@workiva.com>
MAINTAINER Salim Ibrahim <salim.31@gmail.com>

RUN a2enmod rewrite

# install the PHP extensions we need
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev mysql-client git php-soap php5-curl sendmail \
	&& rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd mbstring opcache pdo pdo_mysql pdo_pgsql zip
	
WORKDIR /tmp

#Composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

#Set Composer Paths
RUN export PATH="/home/root/.composer/vendor/bin:$PATH"
RUN echo "export PATH=\"/home/root/.composer/vendor/bin:$PATH\"" >> ~/.bashrc

#Install Drush via composer
RUN composer global require drush/drush:8.*
RUN composer global update
#RUN composer self-update
RUN ln -sf ~/.composer/vendor/bin/drush /usr/bin/drush

EXPOSE 80
EXPOSE 443
#Install Drupal Console
#RUN curl -LSs http://drupalconsole.com/installer | php
#RUN mv console.phar /usr/local/bin/drupal


# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

ENV TERM xterm
WORKDIR /var/www/html
