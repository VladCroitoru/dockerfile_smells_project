FROM node:0.12.7-slim

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        nginx \
        php-apc \
        php5-curl \
        php5-fpm \
        php5-gd \
        php5-memcached \
        php5-mcrypt \
        php5-mysql \
        unzip \
    && apt-get purge -y --auto-remove \
    && apt-get clean autoclean \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/ /var/lib/apt/lists/* /tmp/* /var/tmp/* \

RUN rm -f /etc/nginx/conf.d/default.conf \
    && rm -f /etc/nginx/sites-enabled/default \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /usr/src/app

CMD nginx && php-fpm -F
