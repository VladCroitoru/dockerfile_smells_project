FROM php:8-apache

ENV NODE_VERSION=14.18.1
ENV PATH="/node-v${NODE_VERSION}-linux-x64/bin:${PATH}"

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
	libldap2-dev \
	libsasl2-dev \
        libicu-dev \
        libpq-dev \
        wget \
        ssh \
        libcurl4-openssl-dev \
	libzip-dev \
        postgresql-client \
	sudo \
        python3 \
    && rm -rf /var/lib/apt/lists/* \
    && php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');" \
    && php /tmp/composer-setup.php --install-dir=/usr/local/bin \
    && docker-php-ext-install gd ldap pdo_mysql intl zip curl opcache pdo_pgsql

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini" \
	&& sed -i "s|session.gc_maxlifetime = .*|session.gc_maxlifetime = 86400|g" "$PHP_INI_DIR/php.ini"

COPY app /app
COPY html /html
COPY ./docker/app.php /app/config/app.php.template
COPY ./docker/caps-exec /app/
COPY ./scripts/ssh-tunnel-wrapper.sh /app/

RUN rm -rf /html/node_modules /app/webroot/css/* /app/webroot/js/* \
    && wget -q https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz \
    && tar xJf ./node-v${NODE_VERSION}-linux-x64.tar.xz -C / \
    && rm node-v${NODE_VERSION}-linux-x64.tar.xz \
    && cd /app && php /usr/local/bin/composer.phar install \
    && chown www-data:www-data /app /html /var/www -R \
    && cd /html \ 
    && sudo -u www-data env PATH=${PATH} npm install \ 
    && sudo -u www-data env PATH=${PATH} npm run deploy

WORKDIR /app

CMD './caps-exec'

