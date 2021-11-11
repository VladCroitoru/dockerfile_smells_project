FROM alpine:3.7

MAINTAINER "Eric Ball" <mightynerderic@gmail.com>

RUN apk --update add wget \
    curl \
    git \
    php5 \
    php5-ctype \
    php5-curl \
    php5-dom \
    php5-gd \
    php5-iconv \
    php5-json \
    php5-mysql \
    php5-openssl \
    php5-pdo \
    php5-phar \
    php5-xml \
    php5-xmlreader \
    php5-zip \
    php5-zlib

RUN ln -s `which php5` /usr/bin/php
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

RUN mkdir -p /var/www

WORKDIR /var/www

VOLUME /var/www

RUN composer self-update

CMD ["bash"]

ENTRYPOINT ["composer"]
CMD ["--help"]
