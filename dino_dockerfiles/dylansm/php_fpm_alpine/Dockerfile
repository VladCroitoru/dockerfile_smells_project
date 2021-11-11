# Use Alpine Linux
FROM alpine:edge

# Maintainer
MAINTAINER Dylan Smith <foliomedia@gmail.com>

# Environments
ENV TIMEZONE            America/Los_Angeles
ENV PHP_MEMORY_LIMIT    512M
ENV MAX_UPLOAD          200M
ENV PHP_MAX_FILE_UPLOAD 200
ENV PHP_MAX_POST        200M

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk update && \
    apk upgrade && \
    apk add --update tzdata && \
    cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone && \
    apk add --update \
    imagemagick \
    php7-fileinfo \
    php7-imagick \
    php7-intl \
    php7-mbstring \
    php7-mcrypt \
    php7-soap \
    php7-openssl \
    php7-gmp \
    php7-pdo_odbc \
    php7-json \
    php7-dom \
    php7-pdo \
    php7-zip \
    php7-mysqli \
    php7-sqlite3 \
    php7-pdo_pgsql \
    php7-bcmath \
    php7-gd \
    php7-odbc \
    php7-pdo_mysql \
    php7-pdo_sqlite \
    php7-gettext \
    php7-session \
    php7-xmlreader \
    php7-xmlrpc \
    php7-bz2 \
    php7-iconv \
    php7-pdo_dblib \
    php7-curl \
    php7-ctype \
    php7-fpm && \
    sed -i "s|;*daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf && \
    sed -i "s|;*listen\s*=\s*127.0.0.1:9000|listen = 9000|g" /etc/php7/php-fpm.d/www.conf && \
    sed -i "s|;*listen\s*=\s*/||g" /etc/php7/php-fpm.d/www.conf && \
    sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" /etc/php7/php.ini && \
    sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i" /etc/php7/php.ini && \
    sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i" /etc/php7/php.ini && \
    sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i" /etc/php7/php.ini && \
    sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i" /etc/php7/php.ini && \
    sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php7/php.ini && \
    mkdir /www && \
    apk del tzdata && \
    rm -rf /var/cache/apk/* && \
    addgroup -g 1000 www-data && adduser -u 1000 -h /home/app -s /bin/sh -D -G www-data www-data

RUN chown -R www-data:www-data /var/log/php7

ENV HOME /home/www-data

COPY profile $HOME/.profile
ENV ENV $HOME/.profile

# Set Workdir
WORKDIR /www

# Expose volumes
VOLUME ["/www"]

RUN chown -R www-data:www-data $HOME

USER www-data

# Expose ports
EXPOSE 9000

# Entry point

CMD ["/usr/sbin/php-fpm7"]
# ENTRYPOINT ["/usr/sbin/php-fpm7"]
