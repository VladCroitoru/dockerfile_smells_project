FROM alpine:3.9
MAINTAINER WangXian <xian366@126.com>

WORKDIR /app
# VOLUME /app

# install packages
RUN apk add --update nginx curl openssl wget bash \
        php7-fpm php7-mcrypt php7-mbstring php7-curl php7-gd php7-json php7-openssl php7-opcache \
        php7-xml php7-xmlreader php7-xmlwriter php7-simplexml \
        php7-mysqli php7-session php7-pdo_mysql php7-pdo_sqlite php7-phar php7-iconv php7-soap php7-zip \
        php7-dev autoconf make pkgconf g++ gcc openssl-dev build-base linux-headers \

    && ln -sfv /usr/bin/php7 /usr/bin/php && ln -sfv /usr/bin/php-config7 /usr/bin/php-config && ln -sfv /usr/bin/phpize7 /usr/bin/phpize \
    && apk add tzdata && cp /usr/share/zoneinfo/PRC /etc/localtime && echo "PRC" > /etc/timezone && apk del tzdata \

    && rm -rfv /var/cache/apk/* \

    && cd /tmp \
    && wget https://github.com/igbinary/igbinary/archive/3.1.2.zip \
    && unzip 3.1.2.zip && cd igbinary-3.1.2 \
    && /usr/bin/phpize7 && ./configure --with-php-config=/usr/bin/php-config7 \
    && make && make install \
    && echo extension=igbinary.so >> /etc/php7/conf.d/01_igbinary.ini \

    && cd /tmp \
    && wget https://github.com/phpredis/phpredis/archive/5.3.1.zip \
    && unzip 5.3.1.zip && cd phpredis-5.3.1 \
    && /usr/bin/phpize7 && ./configure --enable-redis-igbinary --with-php-config=/usr/bin/php-config7 \
    && make && make install \
    && echo extension=redis.so >> /etc/php7/conf.d/01_redis.ini \

    && rm -rfv /tmp/* \

    && apk del php7-dev autoconf make pkgconf g++ gcc build-base && php -m

# Copy source to image
ADD . .
RUN rm -rf /app/.git && mv /app/docker/startup.sh /app

ADD docker/nginx.conf /etc/nginx/
ADD docker/php-fpm.conf /etc/php7/

EXPOSE 80 443
CMD ["/bin/sh", "/app/startup.sh"]
