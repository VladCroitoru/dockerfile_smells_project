FROM cheeryfella/php-fpm:latest

MAINTAINER CheeryFella <cheeryfella@gmail.com>

RUN set -ex \
&& apk add --no-cache --virtual .phpize-deps \
		autoconf \
		file \
		g++ \
		gcc \
		libc-dev \
		make \
		pkgconf \
		re2c \
	&& pecl install xdebug \
	&& apk del .phpize-deps \
	&& rm -rf /var/cache/apk/* \
	&& echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20151012/xdebug.so" >> /usr/local/etc/php/php.ini \
	&& touch /usr/local/etc/php/conf.d/xdebug.ini \
	&& echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/xdebug.ini \
	&& echo "xdebug.remote_autostart=1" >> /usr/local/etc/php/conf.d/xdebug.ini \
	&& echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/xdebug.ini \
	&& echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/xdebug.ini \
	&& echo "xdebug.remote_log=/tmp/php-xdebug.log" >> /usr/local/etc/php/conf.d/xdebug.ini \
	&& echo "xdebug.var_display_max_data=-1" >> /usr/local/etc/php/conf.d/xdebug.ini \
	&& echo "xdebug.var_display_max_depth=20" >> /usr/local/etc/php/conf.d/xdebug.ini

CMD ["php-fpm"]
