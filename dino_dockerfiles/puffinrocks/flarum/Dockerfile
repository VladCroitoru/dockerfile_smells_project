FROM php:5-apache

ENV VERSION 0.1.0-beta.5

RUN apt-get update && apt-get install -y \
        curl \
        git \
        libmcrypt-dev \
        libxml2-dev \
        libgd-dev \
        libjpeg62-turbo-dev \
        libpng12-dev \
        mysql-client \
    && docker-php-ext-install -j$(nproc) mbstring zip pdo pdo_mysql json dom fileinfo mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN a2enmod rewrite

RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    chmod +x /usr/local/bin/composer

VOLUME /var/www/html

RUN mkdir -p /usr/src/flarum \
    && cd /usr/src/flarum \
    && composer create-project flarum/flarum . v$VERSION --stability=beta \
    && composer require zendframework/zend-stratigility 1.2.1

RUN cd /usr/src/flarum/vendor/flarum/core \
    && sed -i 's|InfoCommand::class,||g' src/Console/Server.php \
    && sed -i "s|\['config' => \$app->make('flarum.config')\]|['config' => \$app->isInstalled() ? \$app->make('flarum.config') : []]|g" src/Console/Server.php

RUN cd /usr/src/flarum/vendor/flarum/flarum-ext-subscriptions \
    && curl -sSL https://github.com/flarum/flarum-ext-subscriptions/pull/9.diff > 9.diff \
    && git apply 9.diff \
    && cd /usr/src/flarum

COPY config.* /usr/src/flarum/

COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["apache2-foreground"]
