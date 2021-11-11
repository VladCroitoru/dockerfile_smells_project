FROM wordpress:5.6-php7.3-apache
MAINTAINER Glenn Y. Rolland <glenn.rolland@datatransition.net>

# 

VOLUME /var/www/html

RUN sed -i \
    -e 's|exec|chown -R www-data: /var/www/html/wp-content/uploads\nexec|g' \
    /usr/local/bin/docker-entrypoint.sh

RUN curl -L \
	https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
	-o /usr/local/bin/wp && \
	chmod +x /usr/local/bin/wp

RUN mkdir /usr/local/adminer && \
	curl -L \
	https://github.com/vrana/adminer/releases/download/v4.3.1/adminer-4.3.1-mysql-en.php \
	-o /usr/local/adminer/adminer.php && \
	ln -s /usr/local/adminer/adminer.php adminer.php && \
	ln -s /usr/local/adminer/adminer.php /usr/src/wordpress/adminer.php

RUN apt-get update && \
    apt-get install less nano && \
    apt-get autoremove



# COPY ou ADD 

COPY php-uploads.ini /usr/local/etc/php/conf.d/glenux-uploads.ini
COPY php-performance.ini /usr/local/etc/php/conf.d/glenux-performance.ini
COPY wp-config.php /usr/src/wordpress/wp-config.php
# ADD wp-config.php /var/www/html/wp-config.php
COPY .htaccess /usr/src/wordpress/.htaccess


EXPOSE 80
