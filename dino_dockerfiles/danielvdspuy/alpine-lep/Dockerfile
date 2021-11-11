FROM          alpine:latest
MAINTAINER    Daniel van der Spuy <hello@danielvdspuy.co>

# Environment variables
ENV TIMEZONE  Europe/London
ENV PHP_MEMORY_LIMIT    512M
ENV MAX_UPLOAD          50M
ENV PHP_MAX_FILE_UPLOAD 200
ENV PHP_MAX_POST        100M
ENV PHP_MAX_EXEC_TIME   300

# Set timezone
RUN apk add --update tzdata && \
    cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone && \

    # Install global deps
    apk --update --no-cache add \
    curl \
    shadow && \

    # Install php7-fpm, nginx, supervisor
    apk --update --no-cache add \
    nginx \
    php7 \
    php7-fpm \
    php7-zlib \
    php7-curl \
    php7-mcrypt \
    php7-json \
    php7-dom \
    php7-pdo \
    php7-pdo_mysql \
    php7-gd \
    php7-openssl \
    php7-phar \
    php7-mbstring \
    php7-ctype \
    php7-common \
    php7-session \
    php7-xml \
    php7-xmlreader \
    php7-pear \
    php7-dev \
    supervisor \

    # Install deps to compile imagemagick
    autoconf \
    g++ \
    imagemagick-dev \
    libtool \
    make && \

    # PECL XML support
    sed -i "$ s|\-n||g" /usr/bin/pecl && \

    # Install imagick
    pecl install imagick && \
    echo "extension=imagick.so" > /etc/php7/php.ini && \

    # Config php-fpm
    sed -i "s|;*daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf && \
    sed -i "s|;*;clear_env\s*=\s*no|clear_env = no|g" /etc/php7/php-fpm.d/www.conf && \
    sed -i "s|;*user\s*=\s*nobody|user = www-data|g" /etc/php7/php-fpm.d/www.conf && \
    sed -i "s|;*group\s*=\s*nobody|group = www-data|g" /etc/php7/php-fpm.d/www.conf && \
    sed -i "s|;*listen\s*=\s*127.0.0.1:9000|listen = 9000|g" /etc/php7/php-fpm.d/www.conf && \
    sed -i "s|;*listen\s*=\s*/||g" /etc/php7/php-fpm.d/www.conf && \

    # Config php.ini
    sed -i "s|;*expose_php =.*|expose_php = Off|i" /etc/php7/php.ini && \
    sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" /etc/php7/php.ini && \
    sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i" /etc/php7/php.ini && \
    sed -i "s|;*max_execution_time =.*|max_execution_time = ${PHP_MAX_EXEC_TIME}|i" /etc/php7/php.ini && \
    sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i" /etc/php7/php.ini && \
    sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i" /etc/php7/php.ini && \
    sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i" /etc/php7/php.ini && \
    sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php7/php.ini

# Copy configs and scripts
ADD ./supervisor.conf /etc/supervisor/conf.d/supervisor.conf

RUN mkdir -p /etc/nginx && \
    mkdir -p /var/run/php7-fpm && \
    mkdir -p /var/run/nginx && \
    mkdir -p /var/log/supervisor && \

    # Create www-data user and group
    set -x ; \
    addgroup -g 82 -S www-data ; \
    adduser -u 82 -D -S -G www-data www-data && \

    # Set perms for www-data user
    chown -R www-data:www-data /var/www && \

    # Housekeeping
    rm -rf /var/cache/apk/* && \
    apk del --purge \
    tzdata \
    php7-dev \
    php7-pear \
    autoconf \
    g++ \
    libtool \
    make \
    shadow

# Expose volumes
VOLUME ["/var/www"]

COPY ./nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80 9000

# Script entry point
ENTRYPOINT ["supervisord", "--configuration", "/etc/supervisor/conf.d/supervisor.conf"]
