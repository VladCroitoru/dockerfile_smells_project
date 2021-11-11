FROM drupal:8-apache

ARG SITE_INSTALL
ARG XDEBUG_INSTALL
ARG CMS_ENVIRONMENT

RUN apt-get update && apt-get install -y --no-install-recommends \
  ssl-cert \
	curl \
	git \
	mariadb-client \
	vim \
	zip \
	unzip \
	netcat \
	wget

RUN pecl install xdebug

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
  php composer-setup.php && \
  mv composer.phar /usr/local/bin/composer && \
  php -r "unlink('composer-setup.php');"

RUN composer global require drush/drush:10.* && composer global install && ln -s ~/.composer/vendor/bin/drush /usr/bin/drush

RUN rm -rf /var/www/html/*

CMD ["sh", "-c", "/opt/drupal/scripts/install.sh && apache2-foreground"]
