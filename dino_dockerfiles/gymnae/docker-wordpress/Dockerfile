FROM gymnae/webserverbase:latest

# blatantly copied from https://github.com/docker-library/wordpress/blob/master/php7.1/fpm-alpine/Dockerfile
# docker-entrypoint.sh dependencies

RUN apk-install \
# in theory, docker-entrypoint.sh is POSIX-compliant, but priority is a working, consistent image
		bash \
# BusyBox sed is not sufficient for some of our sed expressions
		sed \
# Tar is also not sufficient, install real tar
		tar \

# install the PHP extensions we need
		php7-soap@community \
		php7-opcache@community \
		php7-pear@community \
		php7-xml@community \
		php7-dom@community \
    		php7-ftp@community \
    		php7-exif@community \
    		php7-intl@community \
    		php7-gmp@community \
    		php7-mysqli@community \
		php7-redis@community \
		php7-bz2@community
		
# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=2'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /etc/php7/php.ini

VOLUME /var/www/html

ENV WORDPRESS_VERSION 4.9.4
ENV WORDPRESS_SHA1 0e630bf940fd586b10e099cd9195b3e825fb194c

# prepare directories for wordpress source
RUN mkdir -p /usr/src

RUN set -ex; \
	curl -o wordpress.tar.gz -fSL "https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz"; \
	echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress
	tar -xzf wordpress.tar.gz -C /usr/src/; \
	rm wordpress.tar.gz; \
	chown -R nginx:www-data /usr/src/wordpress

#prepare web dirs	
RUN	mkdir -p /etc/nginx/global &&\
	mkdir -p /etc/nginx/sites-enabled &&\
	mkdir -p /etc/nginx/sites-available &&\
	mkdir -p /var/www/logs &&\
	mkdir -p /var/www/cache &&\
	mkdir -p /var/run/nginx-cache

COPY docker-entrypoint.sh /usr/local/bin/
COPY nginx_conf/sites-available/* /etc/nginx/sites-available/
COPY nginx_conf/nginx.conf /etc/nginx/nginx.conf
COPY nginx_conf/global/* /etc/nginx/global/
COPY nginx_conf/global/server/* /etc/nginx/global/server/

WORKDIR /var/www/html

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["php-fpm7"]
