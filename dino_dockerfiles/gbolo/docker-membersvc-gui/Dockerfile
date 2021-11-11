FROM alpine:edge

MAINTAINER George Bolo <gbolo@linuxctl.com>

EXPOSE 80 443
VOLUME ["/data"]

# -----------------------------------------------------------------------------
# Install required software
# -----------------------------------------------------------------------------
RUN apk add --no-cache bash supervisor mariadb-client nginx \
    php5-fpm php5-pdo php5-json php5-curl php5-pdo_mysql php5-pdo_sqlite php5-openssl

# -----------------------------------------------------------------------------
# Prepare and configure
# -----------------------------------------------------------------------------
RUN mkdir -p /data/nginx/www && \
    mkdir -p /data/nginx/conf && \
    mkdir -p /data/php-fpm/conf

COPY ./docker/nginx.conf /data/nginx/conf/nginx.conf
COPY ./docker/php-fpm.conf /data/php-fpm/conf/php-fpm.conf
COPY ./docker/supervisord.conf /etc/supervisord.conf
COPY ./docker/wrapper.sh /wrapper.sh

COPY ./src /data/nginx/www/

RUN chmod +x /wrapper.sh
CMD ["/wrapper.sh"]

# -----------------------------------------------------------------------------
# run supervisord
# -----------------------------------------------------------------------------
#CMD ["/usr/bin/supervisord"]
