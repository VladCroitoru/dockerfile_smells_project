FROM php:5.6-fpm-alpine

MAINTAINER Kirill Garbar <kirill@iterium.co.uk>

ENV TIMEZONE Europe/London

# persistent / runtime deps
ENV PHPIZE_DEPS \
		autoconf \
		dpkg-dev dpkg \
		file \
		g++ \
		gcc \
		libc-dev \
		make \
		pcre-dev \
		pkgconf \
		re2c

ADD php/php.ini /usr/local/etc/php/

RUN sed -i -e 's/v3\.4/v3\.5/g' /etc/apk/repositories \
    && apk --update upgrade \
    && apk add --no-cache --virtual .persistent-deps \
  		ca-certificates \
  		curl \
  		tar \
  		xz \
  		openssl \
      openssl-dev \
      tzdata \
      runit \
      git \
      nginx \
      libmemcached-dev \
      cyrus-sasl-dev \
      libpng-dev \
    && apk add --no-cache --virtual .build-deps $PHPIZE_DEPS \
    && mkdir /app \
    && curl -L -o /tmp/mongo.tar.gz https://pecl.php.net/get/mongo-1.6.16.tgz \
    && tar xfz /tmp/mongo.tar.gz -C /tmp/ \
    && mkdir -p /usr/src/php/ext/mongo \
    && mv /tmp/mongo-1.6.16/* /usr/src/php/ext/mongo \
    && rm -r /tmp/mongo* \
    && cd /usr/src/php/ext/mongo \
    && phpize \
    && ./configure \
    && make all \
    && docker-php-ext-install mongo \
		&& curl -L -o /tmp/mongodb.tar.gz https://pecl.php.net/get/mongodb-1.3.2.tgz \
		&& tar xfz /tmp/mongodb.tar.gz -C /tmp/ \
		&& mkdir -p /usr/src/php/ext/mongodb \
		&& mv /tmp/mongodb-1.3.2/* /usr/src/php/ext/mongodb \
		&& rm -r /tmp/mongodb* \
		&& cd /usr/src/php/ext/mongodb \
		&& phpize \
		&& ./configure \
		&& make all \
		&& docker-php-ext-install mongodb \
    && curl -L -o /tmp/memcached.tar.gz https://pecl.php.net/get/memcached-2.2.0.tgz \
    && tar xfz /tmp/memcached.tar.gz -C /tmp/ \
    && mkdir -p /usr/src/php/ext/memcached \
    && mv /tmp/memcached-2.2.0/* /usr/src/php/ext/memcached \
    && rm -r /tmp/memcached* \
    && cd /usr/src/php/ext/memcached \
    && phpize \
    && ./configure \
    && make all \
    && docker-php-ext-install memcached gd \
    && docker-php-source delete \
    && apk del .build-deps \
    && cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
    && echo "${TIMEZONE}" > /etc/timezone \
    && rm -rf /var/cache/apk/* \
    && rm /usr/local/etc/php-fpm.d/* \
    && { \
      echo '[global]'; \
      echo 'daemonize = no'; \
      echo; \
      echo '[www]'; \
      echo 'user = nginx'; \
      echo 'group = nginx'; \
      echo ''; \
      echo 'listen = /var/run/php5-fpm.sock'; \
      echo 'listen.mode = 0666'; \
      echo ''; \
      echo 'pm = dynamic'; \
      echo 'pm.max_children = 5'; \
      echo 'pm.start_servers = 2'; \
      echo 'pm.min_spare_servers = 1'; \
      echo 'pm.max_spare_servers = 3'; \
      echo 'pm.max_requests = 500'; \
      echo ''; \
      echo 'chdir = /app'; \
      echo ''; \
      echo '; Ensure worker stdout and stderr are sent to the main error log.'; \
      echo 'catch_workers_output = yes'; \
      echo ''; \
      echo 'clear_env = no'; \
    } | tee /usr/local/etc/php-fpm.d/www.conf \
    && sed -i 's/;daemonize = yes/daemonize = no/g' /usr/local/etc/php-fpm.conf \
    && sed -i 's/;error_log = log\/php5\/error.log/error_log = \/proc\/self\/fd\/2/g' /usr/local/etc/php-fpm.conf \
    && sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /usr/local/etc/php/php.ini \
    && sed -i 's/variables_order = "GPCS"/variables_order = "EGPCS"/g' /usr/local/etc/php/php.ini \
    && mkdir -p /etc/service/nginx \
    && { \
      echo '#!/bin/sh'; \
      echo 'exec 2>&1'; \
      echo 'source /env'; \
      echo 'mkdir -p /run/nginx'; \
      echo 'exec /usr/sbin/nginx -c /etc/nginx/nginx.conf  -g "daemon off;"'; \
    } | tee /etc/service/nginx/run \
    && chmod +x /etc/service/nginx/run \
    && mkdir /etc/service/php5-fpm \
    && { \
      echo '#!/bin/sh'; \
      echo 'exec 2>&1'; \
      echo 'source /env'; \
      echo 'mkdir -p /run/php'; \
      echo 'exec /usr/local/sbin/php-fpm --nodaemonize'; \
    } | tee /etc/service/php5-fpm/run \
    && chmod +x /etc/service/php5-fpm/run \
    && mkdir -p /var/log/nginx \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

ADD nginx/default.conf /etc/nginx/conf.d/default.conf
ADD runit/runit-wrapper /sbin/

# Install Composer
ONBUILD ARG GITHUB_OAUTH_TOKEN

ONBUILD RUN php -r "readfile('https://getcomposer.org/installer');" | php -- --install-dir=/usr/local/bin --filename=composer \
    && composer config -g github-oauth.github.com $GITHUB_OAUTH_TOKEN \
    && composer global require hirak/prestissimo --no-progress --profile --no-suggest --no-interaction

WORKDIR /app

EXPOSE 80

CMD ["/sbin/runit-wrapper"]
