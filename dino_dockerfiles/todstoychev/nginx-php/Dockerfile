FROM todstoychev/nginx:latest

LABEL description="Docker image with nginx and php 7.1.2 compiled."
LABEL maintainer="todstoychev@gmail.com"
LABEL version="0.1.0"

WORKDIR /root
ADD http://be2.php.net/get/php-7.1.2.tar.gz/from/this/mirror php-7.1.2.tar.gz
RUN tar -xvzf php-7.1.2.tar.gz && rm php-7.1.2.tar.gz
WORKDIR /root/php-7.1.2
RUN apt-get update && apt-get install build-essential \
libfcgi-dev \
libfcgi0ldbl \
libjpeg62-turbo-dbg \
libmcrypt-dev \
libssl-dev \
libc-client2007e \
libc-client2007e-dev \
libxml2-dev \
libbz2-dev \
libcurl4-openssl-dev \
libjpeg-dev \
libpng12-dev \
libfreetype6-dev \
libkrb5-dev \
libpq-dev \
libxml2-dev \
libxslt1-dev \
autoconf \
g++ \
make \
unzip \
wget -y

RUN ln -s /usr/lib/libc-client.a /usr/lib/x86_64-linux-gnu/libc-client.a

# Compile and install php7
RUN ./buildconf --force \
&& ./configure --prefix=/opt/php-7.1 \
    --with-pdo-pgsql \
    --with-zlib-dir \
    --with-freetype-dir \
    --enable-mbstring \
    --with-libxml-dir=/usr \
    --enable-soap \
    --enable-calendar \
    --with-curl \
    --with-mcrypt \
    --with-zlib \
    --with-gd \
    --with-pgsql \
    --disable-rpath \
    --enable-inline-optimization \
    --with-bz2 \
    --with-zlib \
    --enable-sockets \
    --enable-sysvsem \
    --enable-sysvshm \
    --enable-pcntl \
    --enable-mbregex \
    --enable-exif \
    --enable-bcmath \
    --with-mhash \
    --enable-zip \
    --with-pcre-regex \
    --with-pdo-mysql \
    --with-mysqli \
    --with-mysql-sock=/var/run/mysqld/mysqld.sock \
    --with-jpeg-dir=/usr \
    --with-png-dir=/usr \
    --enable-gd-native-ttf \
    --with-openssl \
    --with-fpm-user=www-data \
    --with-fpm-group=www-data \
    --with-libdir=/lib/x86_64-linux-gnu \
    --enable-ftp \
    --with-imap \
    --with-imap-ssl \
    --with-kerberos \
    --with-gettext \
    --with-xmlrpc \
    --with-xsl \
    --enable-opcache \
    --enable-fpm \
&& make \
&& make install clean && \
rm -rf php-7.1.2

RUN ln -s /opt/php-7.1/bin/* /usr/bin && ln -s /opt/php-7.1/sbin/* /usr/sbin

# Install redis extension
WORKDIR /root
RUN wget https://github.com/phpredis/phpredis/archive/php7.zip -O phpredis.zip \
&& unzip -o phpredis.zip \
&& rm phpredis.zip \
&& mv phpredis-* phpredis \
&& cd phpredis \
&& phpize \
&& ./configure \
&& make \
&& make install \
&& rm -rf phpredis

# Uninstall the unecessary stuff
RUN apt-get autoremove -y

ADD resources/php.conf /etc/supervisor/conf.d
ADD resources/default /etc/nginx/sites-available/default
ADD resources/php-fpm.conf /opt/php-7.1/etc/php-fpm.conf
ADD resources/www.conf /opt/php-7.1/etc/php-fpm.d/www.conf

RUN rm -rf /root/php-7.1.2 /root/phpredis
RUN mkdir /var/log/php

WORKDIR /app

RUN echo '<?php phpinfo();' > index.php
EXPOSE 80 443

CMD ["/usr/bin/supervisord"]

