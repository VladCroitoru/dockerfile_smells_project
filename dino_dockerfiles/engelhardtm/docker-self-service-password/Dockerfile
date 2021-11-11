FROM alpine:3.6
LABEL Maintainer="Matthias Engelhardt <matthias.engelhardt@accso.de>" \
      Description="Lightweight container ltb-project"

EXPOSE 80

RUN apk --no-cache add \
    php7 \
    php7-fpm \
    php7-xml \
    php7-mbstring \
    php7-mcrypt \
    php7-ldap \
    php7-session \
    php7-iconv \
    nginx \
    supervisor \
    curl \
    ca-certificates

# Configure nginx
COPY assets/nginx.conf /etc/nginx/nginx.conf

# Configure PHP-FPM
COPY assets/fpm-pool.conf /etc/php7/php-fpm.d/z_custom_fpm-pool.conf
COPY assets/php.ini /etc/php7/conf.d/z_custom_php.ini

# Configure supervisord
COPY assets/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV LTB_PROJECT_VERSION 1.0
ENV LTB_PROJECT_SHA256 2666e164f12f3e2f2bd08d7c580ac17d1474ec503e66d8025e0ffeeb4a1eab7e

# Download ltb-project self-service password
RUN curl -s -L -o self-service-password.tar.gz https://github.com/ltb-project/self-service-password/archive/v1.0.tar.gz && \
    echo "${LTB_PROJECT_SHA256}  self-service-password.tar.gz" | sha256sum -c '-'

# Install ltb-project
RUN mkdir -p /var/www/html && \
    tar zxf self-service-password.tar.gz --strip 1 -C /var/www/html && \
    rm self-service-password.tar.gz

# add default config file
COPY assets/config.inc.php /var/www/html/conf/config.inc.php

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
