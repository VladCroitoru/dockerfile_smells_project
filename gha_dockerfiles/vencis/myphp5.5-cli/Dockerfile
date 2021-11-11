FROM php:5.5-cli

RUN apt-get update && apt-get install -y rsync libbz2-dev libfreetype6-dev libjpeg62-turbo-dev \
        libpng-dev libc-client-dev libkrb5-dev libicu-dev libmcrypt-dev libxml++2.6-dev \
        libxslt-dev libgeoip-dev vim less util-linux ca-certificates openssl cron runit \
    && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-install -j$(nproc) bcmath bz2 calendar gd exif gettext imap intl \
        mcrypt mysql mysqli pcntl pdo_mysql shmop sockets sysvmsg sysvsem sysvshm wddx \
        xsl zip opcache \
    && pecl install apfd-1.0.2 geoip-1.1.1 raphf-1.1.2 propro-1.0.2 redis-2.2.8 xdebug-2.5.5 \
        igbinary-2.0.8 json_post-1.0.2 \
    && docker-php-ext-enable apfd geoip raphf propro redis xdebug igbinary json_post \
    && pecl install pecl_http-2.5.5 \
    && docker-php-ext-enable http \
    && rm -r /tmp/* /var/cache/*

RUN echo    "[PHP]\n"\
            "display_errors = off\n"\
            "display_startup_errors = off\n"\
            "error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT\n"\
            "\n"\
            "[Date]\n"\
            "date.timezone = Europe/Prague\n"\
            "\n" > /usr/local/etc/php/php.ini

RUN mkdir /etc/service/cron \
  && echo '#!/bin/sh' > /etc/service/cron/run \
  && echo 'exec /usr/sbin/cron -f' >> /etc/service/cron/run \
  && chmod -R 700 /etc/service/cron/ \
  && chmod 600 /etc/crontab \
  && rm -f /etc/cron.daily/* \
  && rm -f /etc/cron.weekly/*

CMD ["runsv", "/etc/service/cron"]
