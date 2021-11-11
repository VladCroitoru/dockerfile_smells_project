#
# nginx based mini webserver
# with redis client and php-fpm
#

FROM gymnae/alpine-base:master
MAINTAINER Gunnar Falk <docker@grundstil.de>

# #
# add packages
RUN apk add --no-cache \
	php8-fpm \
	nginx \
	nginx-mod-http-redis2 \
	nginx-mod-http-upload-progress \
	nginx-mod-http-geoip \
	nginx-mod-http-cache-purge \
	nginx-mod-http-fancyindex \
	nginx-mod-rtmp \
	php8-openssl \
	#php7-cli@testing \
	php8-curl \
	php8-gd \
	php8-pecl-redis \
	php8-pdo_mysql \
	php8-pgsql \
	libmaxminddb \
	php8-sqlite3 
#	php7-zlib@community
	
# forward request and error logs to docker log collector
RUN 	ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log \
	&& mkdir -p /tmp/nginx \
	&& chown nginx /tmp/nginx 

# add an nginx user to avoid running as root and manage the mountpoint properly
RUN 	addgroup nginx www-data 
#	&& mkdir -p /var/www/localhost/htdocs \
#	&& chown -R nginx:www-data /var/www/localhost/htdocs

# copy the config
COPY nginx.conf /etc/nginx/
COPY php-fpm.conf /etc/php8/php-fpm.conf

EXPOSE 80 443 8080 4443
	
VOLUME ["/var/www/localhost/htdocs"]
# run nginx
CMD /usr/sbin/php-fpm8 ; /usr/sbin/nginx -g "daemon off;"
