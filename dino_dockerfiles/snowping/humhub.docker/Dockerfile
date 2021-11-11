FROM alpine:3.3
ENV HUMHUB_VERSION=v1.2.0

RUN apk add --no-cache \
    php \
    php-fpm \
    php-curl \
	php-pdo_mysql \
	php-zip \
	php-exif \
	php-intl \
	imagemagick \
	php-ldap \
	php-apcu \
	php-memcache \
	php-gd \
	php-cli \
	php-openssl \
	php-phar \
	php-json \
	php-ctype \
	php-iconv \
	php-sqlite3 \
	supervisor \
	nginx \
	sqlite \
	git wget unzip \
	bash \
    && rm -rf /var/cache/apk/*

# Setup humhub
RUN mkdir /app && \
    cd /app && \
    git clone https://github.com/humhub/humhub.git humhub && \
    cd humhub && \
    git checkout $HUMHUB_VERSION

WORKDIR /app/humhub

# Setup the Composer installer
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \
  && curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \
  && php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !== trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL; exit(1); }" \
  && php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin --filename=composer --snapshot \
  && rm -f /tmp/composer-setup.*

COPY config.json /root/.composer/config.json
RUN composer config github-oauth.github.com 7c4e8ff336f463bf79a786d1ca6f17dd26e87d56
RUN composer global require "fxp/composer-asset-plugin:~1.1.0" && \
    composer update

RUN chmod +x protected/yii && \
    chmod +x protected/yii.bat && \
    chown -R nginx:nginx /app/humhub && \
	chown -R nginx:nginx /var/lib/nginx/ && \
	touch /var/run/supervisor.sock && \
	chmod 777 /var/run/supervisor.sock

COPY pool.conf /etc/php-fpm.d/pool.conf
COPY nginx.conf /etc/nginx/nginx.conf
copy supervisord.conf /etc/supervisord.conf

EXPOSE 80

CMD supervisord
