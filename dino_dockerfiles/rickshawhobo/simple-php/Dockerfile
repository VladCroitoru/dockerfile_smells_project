FROM php:7.2.4-fpm

RUN apt-get update && apt-get install -y \
        apt-utils \
        supervisor \
        nginx \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        wget \
        procps \
        libsqlite3-dev \
        zlib1g-dev \

    && docker-php-ext-install pdo_mysql pdo_sqlite mysqli gd json zip opcache \
    && EXPECTED_COMPOSER_SIGNATURE=$(wget -q -O - https://composer.github.io/installer.sig) \
    && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === '${EXPECTED_COMPOSER_SIGNATURE}') { echo 'Composer.phar Installer verified'; } else { echo 'Composer.phar Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php --install-dir=/usr/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

RUN adduser --system --no-create-home --shell /bin/false --group --disabled-login nginx

ADD docker/supervisord.conf /etc/supervisord.conf
ADD docker/default.conf /etc/nginx/sites-enabled/default
ADD docker/www.conf /usr/local/etc/php-fpm.d/www.conf
ADD docker/start.sh /start.sh

RUN chmod a+x /start.sh

EXPOSE 443 80

CMD ["/start.sh"]
