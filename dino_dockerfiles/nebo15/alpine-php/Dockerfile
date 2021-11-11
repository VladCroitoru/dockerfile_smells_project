FROM alpine:3.5

MAINTAINER Nebo#15 support@nebo15.com

ENV REFRESHED_AT=2016-09-28 \
    PHP_VERSION=5.6.30-r0 \
    PHP_MONGO_VERSION=1.6.14-r0 \
    PHP_INI_DIR=/etc/php5 \
    TERM=xterm \
    HOME=/app

# Ensure www-data user exists
RUN set -x && \
    addgroup -g 82 -S www-data && \
    adduser -u 82 -D -S -G www-data www-data

# Create conf.d for PHP configs
RUN mkdir -p $PHP_INI_DIR/conf.d

# Install PHP
RUN apk --no-cache --update add \
        ca-certificates \
        wget \
        php5=$PHP_VERSION \
        php5-fpm=$PHP_VERSION \
        php5-cli \
        php5-pdo \
        php5-zip \
        php5-phar \
        php5-zlib \
        php5-json \
        php5-curl \
        php5-ctype \
        php5-mcrypt \
        php5-openssl \
        php5-xml \
        php5-intl \
        php5-imagick

# Install PHP Mongo extension
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-php5-mongo/master/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-php5-mongo/releases/download/1.16.4-r0/php5-mongo-$PHP_MONGO_VERSION.apk && \
    apk --no-cache add php5-mongo-$PHP_MONGO_VERSION.apk && \
    rm php5-mongo-1.6.14-r0.apk

# Install Composer via https://getcomposer.org/download/
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/local/bin/composer

# Clean build
RUN apk del wget && \
    rm -rf /var/cache/apk/*

# Add entrypoint
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

# Tune PHP configs
COPY php.ini /etc/php5/conf.d/www-setting.ini
COPY php-fpm.conf /etc/php5/php-fpm.conf

# Fix paths access rights
RUN touch /var/log/php-fpm.log && \
    chmod 700 /var/log/php-fpm.log && \
    chown www-data:www-data /var/log/php-fpm.log && \
    chown www-data:www-data $HOME

RUN cd ${HOME}
WORKDIR ${HOME}

# Export PHP-FPM port
EXPOSE 9000

CMD ["php-fpm", "-F"]
