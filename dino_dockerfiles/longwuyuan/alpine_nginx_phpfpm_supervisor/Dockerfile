From alpine

COPY conf/. /tmp

RUN apk -U update && \
    apk upgrade && \
    apk add curl tcpdump lsof iperf nmap openssh-client \
    bash \
    gettext \
    tzdata \
    make \
    pcre-dev \
    pkgconf \
    re2c \
    libpng-dev \
    libjpeg-turbo-dev \
    freetype-dev \
    openssl-dev \
    libmcrypt-dev \
    librdkafka-dev \
    tar \
    xz \
    ca-certificates \
    php7 \
    php7-dom \
    php7-gettext \
    php7-fpm \
    php7-mysqlnd \
    php7-mysqli \
    php7-mcrypt \
    php7-gd \
    php7-curl \
    php7-common \
    php7-json \
    php7-xml \
    php7-mbstring \
    php7-pdo_mysql \
    php7-zip \
    php7-phar \
    php7-opcache \
    php7-openssl \
    php7-session \
    php7-zlib \
    nginx \
    supervisor && \
    mkdir -p /code /etc/supervisor.d /run/php /var/log/supervisord /run/nginx/ /var/log/nginx/site && \
    touch /var/log/php7/fpm_error.log /var/log/nginx/site/access.log /var/log/nginx/site/error.log && \
    rm -f /etc/supervisord.conf /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf /etc/php7/php.ini /etc/php7/php-fpm.d/www.conf  && \
# Copy our custom nginx & fpm config (scraped from current infrastructure but still lots to scrape)
    mv /tmp/supervisord.conf /etc/supervisord.conf && \
    mv /tmp/nginx.conf /etc/nginx/nginx.conf && \
    mv /tmp/default.conf /etc/nginx/conf.d/default.conf && \
    mv /tmp/listener.php /listener.php && \
    mv /tmp/php.ini /etc/php7/php.ini && \
    mv /tmp/www.conf /etc/php7/php-fpm.d/www.conf && \
    mv /tmp/phptest.php /var/www/localhost/htdocs/phptest.php

EXPOSE 80

CMD /usr/bin/supervisord
