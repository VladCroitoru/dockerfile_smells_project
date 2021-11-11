FROM ubuntu:16.04
RUN apt-get update && apt-get install -y \
	curl\
	nginx \
	git \
	zip \
	unzip \
	vim \
	htop \
	php-memcache \ 
	php7.0-curl \
	php7.0-gd \
	php7.0-mysql \
	php7.0-pgsql \
	php7.0-sqlite3 \
	php7.0-bcmath \
	php7.0-fpm \
	php7.0-mbstring \
	php7.0-mcrypt \
	php7.0-xml \
	php7.0-zip \
	&& apt-get clean
COPY . /var/www/
COPY deploy/nginx.conf /etc/nginx/
RUN mkdir -p /run/php && touch /var/log/php7.0-fpm.log && chown -R www-data:www-data /var/www /run/php /var/log/php7.0-fpm.log
USER www-data
RUN cd /tmp && curl -sS https://getcomposer.org/installer | php
#COPY parameters.yml /var/www/app/config/parameters.yml
RUN cd /var/www && /tmp/composer.phar install
USER root
EXPOSE 80
CMD php-fpm7.0 && nginx -g "daemon off;"
