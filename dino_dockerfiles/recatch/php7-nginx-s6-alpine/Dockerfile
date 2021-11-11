FROM php:7.2-fpm-alpine

EXPOSE 80 443

RUN apk --no-cache add bind-tools binutils bash curl ca-certificates git tzdata

ENV APP_ENV prod
ENV S6_OVERLAY_VERSION v1.21.8.0
ENV NGINX_VERSION 1.14.2
ENV XDEBUG_VERSION 2.6.1
ENV PHPREDIS_VERSION 4.2.0

RUN curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz | tar xfz - -C /

RUN docker-php-source extract \
    && apk add --no-cache --virtual .php-ext-build-deps \
        $PHPIZE_DEPS \
        freetype-dev \
        libjpeg-turbo-dev \
        libpng-dev \
        libwebp-dev \
        gmp-dev \
        icu-dev \
        libxml2-dev \
        libxslt-dev \
    && apk add --no-cache --virtual .php-ext-deps \
        freetype \
        libjpeg-turbo \
        libpng \
        libwebp \
        gmp \
        icu \
        libxml2 \
        libxslt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-webp-dir=/usr/include/ --with-png-dir=/usr/include/ \
    && docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" bcmath exif gd gmp intl mysqli opcache pcntl pdo_mysql soap sockets xmlrpc xsl zip \
    && pecl install redis-${PHPREDIS_VERSION} \
    && pecl install xdebug-${XDEBUG_VERSION} \
    && docker-php-ext-enable redis \
    && apk del .php-ext-build-deps \
    && docker-php-source delete

RUN addgroup -S nginx \
    && adduser -D -S -h /home/nginx -s /sbin/nologin -G nginx nginx \
    && build_pkgs="build-base linux-headers openssl-dev pcre-dev zlib-dev" \
    && runtime_pkgs="openssl openssh-client pcre zlib" \
    && apk --no-cache add ${build_pkgs} ${runtime_pkgs} \
    && mkdir -p /usr/src \
    && mkdir -p /var/cache/nginx \
    && chown -R nginx: /var/cache/nginx \
    && curl -sSL https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar xfz - -C /usr/src \
    && cd /usr/src/nginx-${NGINX_VERSION} \
    && ./configure \
       --prefix=/etc/nginx \
       --sbin-path=/usr/sbin/nginx \
       --conf-path=/etc/nginx/nginx.conf \
       --error-log-path=/var/log/nginx/error.log \
       --http-log-path=/var/log/nginx/access.log \
       --pid-path=/var/run/nginx.pid \
       --lock-path=/var/run/nginx.lock \
       --http-client-body-temp-path=/var/cache/nginx/client_temp \
       --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
       --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
       --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
       --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
       --user=nginx \
       --group=nginx \
       --with-http_ssl_module \
       --with-http_realip_module \
       --with-http_addition_module \
       --with-http_sub_module \
       --with-http_dav_module \
       --with-http_mp4_module \
       --with-http_gunzip_module \
       --with-http_gzip_static_module \
       --with-http_random_index_module \
       --with-http_secure_link_module \
       --with-http_stub_status_module \
       --with-http_auth_request_module \
       --with-file-aio \
       --with-ipv6 \
       --with-threads \
       --with-stream \
       --with-stream_ssl_module \
       --with-stream_realip_module \
       --with-http_slice_module \
       --with-compat \
       --with-http_v2_module \
    && make -j"$(getconf _NPROCESSORS_ONLN)" \
    && make install \
    && rm -Rf /etc/nginx \
    && strip /usr/sbin/nginx* \
    && rm -rf /usr/src/nginx-${NGINX_VERSION} \
    && apk --no-cache del ${build_pkgs} \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN curl -sSL https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

ADD root /

RUN chown -R nginx: /home/nginx \
    && update-ca-certificates

WORKDIR /data

ENTRYPOINT []
CMD ["/init"]
