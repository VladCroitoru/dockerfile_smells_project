# OS alpine 3.13
FROM nginx:1.19.8-alpine

# alpine & nginx version
RUN cat /etc/os-release | grep PRETTY_NAME && nginx -v

# build arguments
ARG timezone="America/Santiago"

# packages
RUN apk update && apk add --no-cache \
	bash \
	supervisor \
	tzdata \
	gettext \
	curl \
	# php
	php7 \
	php7-curl \
	php7-dom \
	php7-fileinfo \
	php7-fpm \
	php7-gd \
	php7-gettext \
	php7-json \
	php7-mbstring \
	php7-openssl \
	php7-pdo \
	php7-phar \
	php7-psr \
	php7-opcache \
	php7-session \
	php7-simplexml \
	php7-tokenizer \
	php7-xml \
	php7-zlib \
	&& rm -rf /var/cache/apk/*

# directory links
RUN ln -sf /etc/php7 /etc/php && \
	ln -sf /usr/bin/php7 /usr/bin/php && \
	ln -sf /usr/sbin/php-fpm7 /usr/bin/php-fpm && \
	ln -sf /usr/lib/php7 /usr/lib/php

# timezone
ENV TZ=$timezone \
	COMPOSER_ALLOW_SUPERUSER=1

RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && date

# php composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# set www-data group (82 is the standard uid/gid for www-data in Alpine)
RUN set -x; \
	addgroup -g 82 -S www-data; \
	adduser -u 82 -D -S -G www-data www-data && exit 0; exit 1

# prepare folders
RUN rm /etc/nginx/conf.d/default.conf && \
	mkdir -p /var/www/public /var/log/supervisord

# copy files
COPY bashrc /root/.bashrc
COPY supervisord.conf /etc/supervisord.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx-sites.conf /etc/nginx/sites-enabled/default
COPY php-fpm.conf /etc/php7/php-fpm.d/www.conf
COPY index.php /var/www/public
COPY start /root/start

# expose
EXPOSE 80

# entrypoint
ENTRYPOINT ["/root/start"]
