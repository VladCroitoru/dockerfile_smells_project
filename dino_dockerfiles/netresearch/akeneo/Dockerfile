FROM php:5.6-apache

RUN apt-get update \
    && apt-get install -y --no-install-recommends libicu-dev libmcrypt-dev libpng-dev libcurl3-dev libxml2-dev libjpeg-dev libpng-dev libssl-dev mysql-client \
    && docker-php-ext-configure intl \
    && docker-php-ext-configure gd --enable-gd-native-ttf --with-jpeg-dir=/usr/lib/x86_64-linux-gnu --with-png-dir=/usr/lib/x86_64-linux-gnu \
    && docker-php-ext-install mbstring pdo_mysql mysqli intl mcrypt gd exif curl soap zip opcache bcmath \
    && pecl install -f mongo \
    && pecl install apcu-4.0.11 \
    && docker-php-ext-enable mongo apcu \
    && apt-get autoremove \
    && apt-get clean -y \
    && rm -rf /tmp/* \
    && rm -rf /var/tmp/* \
    && for logs in `find /var/log -type f`; do > $logs; done \
    && rm -rf /usr/share/locale/* \
    && rm -rf /usr/share/man/* \
    && rm -rf /usr/share/doc/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /var/cache/apt/*.bin

RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

COPY setup/ /

RUN a2enmod rewrite \
    && a2ensite akeneo_pim \
    && a2dissite 000-default.conf

ARG AKENEO_VERSION=1.7.6

RUN mkdir -p /src/packages/akeneo/pim-community-dev \
    && cd /src/packages/akeneo/pim-community-dev \
    && curl -sL https://github.com/akeneo/pim-community-dev/archive/v${AKENEO_VERSION}.tar.gz | tar -xz --strip-components=1 \
    && php -r '\
        $json = json_decode(file_get_contents("composer.json"), true); \
        $json["version"] = getenv("AKENEO_VERSION"); \
        file_put_contents("composer.json", json_encode($json, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . "\n");'

WORKDIR /var/www/html

RUN chmod +x /usr/local/bin/akeneo-entrypoint

RUN composer create-project --no-install akeneo/pim-community-standard . $AKENEO_VERSION \
    && composer config preferred-install 'dist' \
    && php -r '\
        $json = json_decode(file_get_contents("composer.json"), true); \
        $json["repositories"] = [["type" => "path", "url" => "/src/packages/*/*"]]; \
        file_put_contents("composer.json", json_encode($json, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . "\n");' \
    && composer require doctrine/mongodb-odm-bundle

RUN curl -sL "https://raw.githubusercontent.com/netresearch/retry/master/retry" -o /usr/local/bin/retry \
    && chmod +x /usr/local/bin/retry

RUN chmod 777 /usr/local/bin/*

ENTRYPOINT ["akeneo-entrypoint"]

CMD ["apache2-foreground"]
