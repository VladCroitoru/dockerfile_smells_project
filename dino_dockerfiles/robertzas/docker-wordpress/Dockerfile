FROM alpine:3.7

ENV SSH_PASSWD "root:Docker!"

RUN set -ex \
    && addgroup -S www-data \
    && adduser -D -H -S -G www-data www-data\
    \
    && addgroup -S memcached \
    && adduser -D -H -S -G memcached memcached

# Install packages from stable repo's
RUN set -ex \
    && apk --no-cache upgrade \
    && apk --no-cache add \
    supervisor \
    curl \
    bash \
    # Setup SSH
    openssh \
    && /usr/bin/ssh-keygen -A \
    && echo "$SSH_PASSWD" | chpasswd 
COPY config/sshd_config /etc/ssh/


# Install packages from testing repo's
RUN set -ex \
    && apk --no-cache add \
    php7 \
    php7-fpm \
    php7-mysqli \
    php7-json \
    php7-openssl \
    php7-curl \
    php7-zip \
    php7-xml \
    php7-phar \
    php7-intl \
    php7-dom \
    php7-simplexml \
    php7-xmlreader \
    php7-ctype \
    php7-mbstring \
    php7-gd \
    php7-memcached \
    memcached \
    php7-opcache \
    nginx \
    nginx-mod-http-cache-purge \
    mariadb \
    mariadb-client \
    mariadb-common
    # mariadb \
    # mariadb-client \
    # --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ \
    # --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ \
    # --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/

# Wordpress
ENV WORDPRESS_VERSION 4.9.4
ENV WORDPRESS_SHA1 0e630bf940fd586b10e099cd9195b3e825fb194c

RUN set -ex \
    && mkdir -p /usr/src

# Upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress
RUN set -ex \
    && curl -o wordpress.tar.gz -SL https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz \
    && echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \
    && tar -xzf wordpress.tar.gz -C /usr/src/ \
    && rm wordpress.tar.gz \
    && chown -R www-data:www-data /usr/src/wordpress

# Copy WP config
COPY config/wp-secrets.php /usr/src/wordpress
COPY config/wp-config.php /usr/src/wordpress
RUN set -ex \
    && chown -R www-data:www-data /usr/src/wordpress \
    && chmod -R 777 /usr/src/wordpress

# Copy other configs
COPY config/nginx.conf          /usr/src/wordpress/nginx.conf
COPY config/fpm-pool.conf       /etc/php7/php-fpm.d/zzz_custom.conf
COPY config/php.ini             /etc/php7/conf.d/zzz_custom.ini
COPY config/supervisord.conf    /etc/supervisor/conf.d/supervisord.conf
COPY config/my.cnf              /etc/mysql/my.cnf

# Make logs dir
RUN set -ex \
    && mkdir -p /home/LogFiles/

# Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN set -ex \
    && chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

EXPOSE 2222 3306 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
