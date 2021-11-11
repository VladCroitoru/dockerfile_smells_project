FROM alpine:latest
MAINTAINER Antonio Dal Sie <antonydalsie@gmail.com>

WORKDIR /tmp

RUN apk update \
    && apk --no-cache add \
        bash \
        ca-certificates \
        curl \
        unzip \
        php7 \
        php7-xml \
        php7-exif \
        php7-zip \
        php7-xmlreader \
        php7-xmlwriter \
        php7-zlib \
        php7-opcache \
        php7-mcrypt \
        php7-openssl \
        php7-curl \
        php7-json \
        php7-dom \
        php7-phar \
        php7-mbstring \
        php7-bcmath \
        php7-pdo \
        php7-pdo_pgsql \
        php7-pdo_sqlite \
        php7-pdo_mysql \
        php7-soap \
        php7-xdebug \
        php7-pcntl \
        php7-session \
        php7-session \
        php7-ctype \
        php7-tokenizer \
        nodejs-npm \
    && apk add -u yarn \
    && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --install-dir=/usr/bin --filename=composer \
    && php -r "unlink('composer-setup.php');" \

    # Enable X-Debug
    && sed -i 's/\;z/z/g' /etc/php7/conf.d/xdebug.ini \
    && php -m | grep -i xdebug

COPY start.sh /tmp/start.sh
COPY db.sh /tmp/db.sh

RUN apk --no-cache add \
        mariadb \
        mariadb-client \
    && chmod 744 /tmp/start.sh \
    && chmod 744 /tmp/db.sh \
    && /usr/bin/mysql_install_db --user=mysql \
    && ln -s /usr/share/mysql/mysql.server /etc/init.d/mysql \
    && /etc/init.d/mysql start \
    && /tmp/db.sh

VOLUME ["/app"]
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["/tmp/start.sh"]