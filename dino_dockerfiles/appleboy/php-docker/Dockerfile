FROM alpine:3.3

MAINTAINER Bo-Yi Wu <appleboy.tw@gmail.com>

RUN apk update \
  && apk add bash mysql-client ca-certificates

# Install php 7
RUN apk add php7 php7-fpm php7-json php7-zlib php7-xml php7-pdo php7-phar php7-openssl \
  php7-pdo_mysql php7-mysqli php7-session \
  php7-mcrypt php7-curl php7-opcache php7-ctype  php7-xdebug \
  php7-bcmath php7-dom php7-xmlreader php7-mbstring \
  --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

RUN ln -s /usr/bin/php7 /usr/bin/php

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
RUN rm -rf /var/cache/apk/*

RUN mkdir -p /var/www

# Add volumes
VOLUME ["/var/www"]

# Set the work directory
WORKDIR /var/www

CMD ["php", "-a"]
