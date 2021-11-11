FROM alpine:latest

#RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
#    && echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
#    && apk update && apk upgrade \
RUN apk update && apk upgrade \
    && apk add \
    php7 \
    nginx \
    supervisor \
    php7-pdo_mysql \
    php7-mcrypt \
    php7-fpm \
    php7-iconv \
    php7-mbstring \
    php7-opcache \
    curl \
    php7-json \
    php7-phar \
    php7-openssl \
    php7-zip\
    php7-session \
    php7-apcu \
    php7-ctype \
    bash \
    ca-certificates \
    php7-zlib \
    php7-gd \
    php7-xml \
    php7-dom \
    nodejs \
    nodejs-npm \
    php7-curl \
    php7-redis \
    php7-mysqli \
    php7-fileinfo \
    php7-simplexml \
    git \
    ca-certificates \
    php7-tokenizer \
    && mkdir -p /usr/local/composer/bin \
    && curl -sS https://getcomposer.org/installer \
    | /usr/bin/php7 -- --install-dir=/usr/local/composer/bin/ --filename=composer \
    && apk del gcc musl-dev linux-headers libffi-dev augeas-dev \
    && rm -rf /var/www/* \
    /usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp /root/.gnupg \
    /usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html \
    && sed -i -e s-nginx:x:100:101:nginx:/var/lib/nginx:/sbin/nologin-nginx:x:1001:101:nginx:/var/lib/nginx:/sbin/nologin- /etc/passwd \
    && chown -R nginx.nginx /var/lib/nginx \
    && update-ca-certificates

expose 80
