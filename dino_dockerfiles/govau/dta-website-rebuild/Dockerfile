FROM drupal:8.4-apache

RUN apt-get update && apt-get install -y \
	curl \
	git \
	jq \
	vim \
	wget \
	libbz2-dev \
	libfontconfig \
	libpng-dev; \
	docker-php-ext-install bz2 gd;
# Install composer
RUN set -ex; \
	php -r "copy('https://getcomposer.org/download/1.6.3/composer.phar', 'composer.phar');" && \
	php -r "if (hash_file('SHA256', 'composer.phar') === '52cb7bbbaee720471e3b34c8ae6db53a38f0b759c06078a80080db739e4dcab6') { echo 'composer.phar verified'; } else { echo 'composer.phar corrupt'; unlink('composer.phar'); } echo PHP_EOL;" &&\
	install -m 755 composer.phar /usr/local/bin/composer

# We remove the drupal that comes from the base Dockerfile, and expect our local
# code to be mounted at /app

RUN set -ex; \
	rm -rf /var/www/html/*; \
	{ \
		echo '<VirtualHost *:80>'; \
		echo '  ServerAdmin webmaster@localhost'; \
		echo '  DocumentRoot /app/docroot'; \
		echo '  <Directory /app/docroot>'; \
		echo '    AllowOverride All'; \
		echo '    Require all granted'; \
		echo '  </Directory>'; \
		echo '  ErrorLog ${APACHE_LOG_DIR}/error.log'; \
		echo '  CustomLog ${APACHE_LOG_DIR}/access.log combined'; \
		echo '</VirtualHost>'; \
	} > /etc/apache2/sites-enabled/000-default.conf;

VOLUME /app

WORKDIR /app

USER root

# Add the vendor bin folder to PATH.
# Drush also requires mysql-client, and we could use apt's mysql-client, but this
# would not match what is currently deployed to cloud.gov.au. So instead we
# will use the vendor'd mysql client files.
# TODO change to use https://github.com/cloudfoundry/apt-buildpack
ENV PATH="/app/bin:/app/scripts/mysql:${PATH}"

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
