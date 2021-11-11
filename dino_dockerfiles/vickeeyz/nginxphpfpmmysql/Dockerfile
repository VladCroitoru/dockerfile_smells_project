FROM debian:jessie

MAINTAINER Vikrant Kamble <k.vikrantt@gmail.com>

ENV NGINX_VERSION 1.6.2
ENV PHP_VERSION 5.6.30

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        ca-certificates \
        nginx=${NGINX_VERSION}* \
        php5-fpm=${PHP_VERSION}* \
        php5-mysqlnd \
        php5-curl \
        php5-gd \
        php5-intl \
        php-pear \
        php5-imagick \
        php5-imap \
        php5-mcrypt \
        php5-memcache \
        php5-snmp \
        php5-xmlrpc \
        php5-xsl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    ln -sf /dev/stderr /var/log/php-fpm.log

COPY nginx.conf /etc/nginx/

COPY default.conf /etc/nginx/conf.d/

COPY www.conf /etc/php5/fpm/pool.d/

EXPOSE 80

COPY run.sh /

RUN chmod +x /run.sh



CMD ["/run.sh"]
