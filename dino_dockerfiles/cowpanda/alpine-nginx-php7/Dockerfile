FROM bytepark/alpine-nginx:latest

# Add PHP 7
RUN apk upgrade -U && \
    apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add \
    php7 \
    php7-xml \
    php7-xsl \
    php7-pdo_mysql \
    php7-mcrypt \
    php7-curl \
    php7-json \
    php7-fpm \
    php7-phar \
    php7-openssl \
    php7-mysqli \
    php7-ctype \
    php7-opcache \
    php7-mbstring \
    php7-gd \
    php7-posix \
    php7-session \
    php7-iconv 

COPY /rootfs /

# Small fixes
RUN ln -s /etc/php7 /etc/php && \
    ln -s /usr/bin/php7 /usr/bin/php && \
    ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \
    ln -s /usr/lib/php7 /usr/lib/php && \
    rm -fr /var/cache/apk/*

# Install composer global bin
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

# ADD SOURCE
ONBUILD COPY ./src /usr/share/nginx/html
ONBUILD RUN chown -Rf nginx:nginx /usr/share/nginx/html

# Setup Volume
VOLUME ["/usr/share/nginx/html"]

ENTRYPOINT ["/init"]
