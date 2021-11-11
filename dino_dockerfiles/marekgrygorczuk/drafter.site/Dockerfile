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
	acl \
	&& apt-get clean
COPY . /var/www/
COPY deploy/nginx.conf /etc/nginx/
RUN mkdir -p /run/php && touch /var/log/php7.0-fpm.log && chown -R www-data:www-data /var/www /run/php /var/log/php7.0-fpm.log
RUN cd /var/www && setfacl -R -m u:www-data:rwX var && setfacl -dR -m u:www-data:rwX var
USER www-data
RUN cd /tmp && curl -sS https://getcomposer.org/installer | php
#COPY parameters.yml /var/www/app/config/parameters.yml
RUN cd /var/www && /tmp/composer.phar install
RUN cd /var/www && php bin/console doctrine:database:create
RUN cd /var/www && php bin/console doctrine:schema:update --force
VOLUME /var/www/app/Resources/database
VOLUME /var/www/app/var/cache
USER root
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log
# forward Symphony logs logs to docker log collector
RUN ln -sf /dev/stdout /var/www/var/logs/prod.log
RUN ln -sf /dev/stdout /var/log/php7.0-fpm.log
EXPOSE 80
CMD cd /var/www && php bin/console doctrine:schema:update --force && php-fpm7.0 && nginx -g "daemon off;"
