FROM fedorza/alpine_36_onb
MAINTAINER Clint Beacock <clint@therefore.ca>/Fedor Zakharov <fedor@therefore.ca>

ENV HENCE_APP_DIR=$HENCE_PREFIX/php5 \
    HENCE_APP_NAME=php \
    HENCE_APP_USER=hence \
    HENCE_APP_VERSION=3.6

ENV HENCE_APP_VOL_PREFIX=/hence/$HENCE_APP_NAME \
    PATH=$HENCE_APP_DIR/bin:$PATH

ENV COMPOSER_HOME=/root/.composer \
    TERM=xterm

RUN apk --update add \
    php5-fpm \
    php5-cli \
    php5-ctype \
    php5-curl \
    php5-dom \
    php5-gd \
    php5-iconv \
    php5-intl@edge \
    php5-json \
    php5-ldap \
    php5-mcrypt \
    php5-memcache \
    php5-mysql \
    php5-mysqli \
    php5-openssl \
    php5-opcache \
    php5-pdo \
    php5-pdo_mysql \
    php5-pdo_pgsql \
    php5-pdo_sqlite \
    php5-pear \
    php5-pgsql \
    php5-phar \
    php5-sockets \
    php5-sqlite3 \
    php5-xml \
    php5-zip \
    php5-zlib \
    git \
    pdftk@edge \
#    build-base  \
    mariadb-common \
    mariadb-client && \
    rm -rf /var/cache/apk/*

COPY rootfs /

RUN curl -sS https://getcomposer.org/installer \
  | php -- --install-dir=/usr/bin --filename=composer

RUN sh $HENCE_PREFIX/install.sh && \
    s6-rmrf /etc/s6/services/s6-fdholderd/down

RUN echo nameserver 8.8.8.8 > /etc/resolve.conf && composer global require drush/drush:8.1.2 && \
    composer global require fillup/phpmyadmin-minimal:4.4.13.1 && \
    ln -sf $COMPOSER_HOME/vendor/bin/drush.php /usr/bin/drush && \
    curl https://drupalconsole.com/installer -L -o drupal.phar && \
    mv drupal.phar /usr/bin/drupal && \
    chmod +x /usr/bin/drupal && \
    drupal init --destination /etc/console -q

EXPOSE 9000
EXPOSE 22

VOLUME ["/etc/php5/custom.d", "/app", "$HENCE_APP_VOL_PREFIX/conf", "$HENCE_APP_VOL_PREFIX/logs/php-general-logs", "$HENCE_APP_VOL_PREFIX/logs/php-error-logs","/vendor", "/config"]

WORKDIR /app
