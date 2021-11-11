FROM  php:fpm-alpine
MAINTAINER Philip G <gp@gpcentre.net>

ENV HOME /root
ENV TERM xterm

RUN apk add --update --no-cache --virtual .build-deps $PHPIZE_DEPS
## All my custom php configurations. Need these lib items for gd.
RUN echo @testing http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && \
    sed -i -e "s/v3.4/edge/" /etc/apk/repositories && \
    apk add --update --no-cache \
    libjpeg-turbo-dev libpng-dev libmcrypt-dev openssl-dev supervisor nginx python python-dev libffi-dev \
# py2-pip is only in the edge repo
    py2-pip 

RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) gd opcache pdo_mysql mcrypt \
	&& pecl install xdebug-2.5.0 \
	&& docker-php-ext-enable xdebug \
	&& runDeps="$( \
		scanelf --needed --nobanner --recursive \
			/usr/local/lib/php/extensions \
			| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
			| sort -u \
			| xargs -r apk info --installed \
			| sort -u \
	)" && \
	pip install -U pip && \
    pip install -U certbot && \
    mkdir -p /etc/letsencrypt/webrootauth

RUN apk del .build-deps

################################
# I really like richarvey/nginx-php-fpm's ideas. BUT, they don't have php7.1 
# 	as Alpine doesn't officially have 7.1 yet, either. Because of this, I'm going 
# 	to meld richarvey/nginx-php-fpm's ideas on a php7.1 version. Sorry for the direct 
# 	copy/paste. For anybody not wanting php7.1, pease use richarvey/nginx-php-fpm.
# 	Repo:  https://github.com/ngineered/nginx-php-fpm/blob/master/Dockerfile
# 
# I'm removing git pull/push support to give you a reason to stick with richarvey/nginx-php-fpm.

ADD etc/supervisord.conf /etc/supervisord.conf

# Copy our nginx config
#RUN rm -Rf /etc/nginx/nginx.conf
ADD etc/nginx/nginx.conf /etc/nginx/nginx.conf
ADD etc/php.ini /usr/local/etc/php/php.ini

# nginx site conf
RUN mkdir -p /etc/nginx/sites-available/ && \
mkdir -p /etc/nginx/sites-enabled/ && \
mkdir -p /etc/nginx/ssl/ && \
rm -Rf /var/www/* && \
mkdir /var/www/html/
ADD etc/nginx/sites-available /etc/nginx/sites-available
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf
RUN rm -f /etc/nginx/conf.d/default.conf

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && chown -R www-data /var/lib/nginx

# Add Scripts
ADD scripts/start.sh /start.sh
ADD scripts/letsencrypt-setup /usr/bin/letsencrypt-setup
ADD scripts/letsencrypt-renew /usr/bin/letsencrypt-renew
RUN chmod 755 /usr/bin/letsencrypt-setup && \
	chmod 755 /usr/bin/letsencrypt-renew && \
	chmod 755 /start.sh

RUN mkdir -p /var/lib/php-fpm
COPY etc/php-fpm/php-fpm.d/zz-docker.conf /usr/local/etc/php-fpm.d/zz-docker.conf
COPY etc/php-fpm/conf.d/zz-docker.ini /usr/local/etc/php/conf.d/zz-docker.ini

EXPOSE 443 80

WORKDIR /var/www

CMD ["/start.sh"]