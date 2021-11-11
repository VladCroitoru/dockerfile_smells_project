FROM buildpack-deps:jessie
MAINTAINER Slawek Kolodziej <hfrntt@gmail.com>

RUN apt-get update && apt-get install -y curl && rm -r /var/lib/apt/lists/*

RUN rm -rf /var/www/html \
 && mkdir -p \
    /var/www/html \
 && chown -R www-data:www-data \
    /var/www/html

RUN gpg --keyserver pgp.mit.edu --recv-keys 0B96609E270F565C13292B24C13C70B87267B52D 0A95E9A026542D53835E3F3A7DEC4E69FC9C83D7

ENV GPG_KEYS 0B96609E270F565C13292B24C13C70B87267B52D 0A95E9A026542D53835E3F3A7DEC4E69FC9C83D7 0E604491
RUN set -xe \
 && for key in $GPG_KEYS; do \
      gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
    done

# compile openssl, otherwise --with-openssl won't work
RUN CFLAGS="-fPIC" && OPENSSL_VERSION="1.0.2d" \
 && cd /tmp \
 && mkdir openssl \
 && curl -sL "https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz" -o openssl.tar.gz \
 && curl -sL "https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz.asc" -o openssl.tar.gz.asc \
 && gpg --verify openssl.tar.gz.asc \
 && tar -xzf openssl.tar.gz -C openssl --strip-components=1 \
 && cd /tmp/openssl \
 && ./config shared && make && make install \
 && rm -rf /tmp/*

ENV PHP_VERSION 5.3.29
ENV PHP_INI_DIR /usr/local/lib

RUN mkdir -p $PHP_INI_DIR/conf.d

# php 5.3 needs older autoconf
RUN set -x \
 && apt-get update && apt-get install -y autoconf2.13 zlib1g zlib1g-dev && rm -r /var/lib/apt/lists/* \
 && curl -SLO http://launchpadlibrarian.net/140087283/libbison-dev_2.7.1.dfsg-1_amd64.deb \
 && curl -SLO http://launchpadlibrarian.net/140087282/bison_2.7.1.dfsg-1_amd64.deb \
 && dpkg -i libbison-dev_2.7.1.dfsg-1_amd64.deb \
 && dpkg -i bison_2.7.1.dfsg-1_amd64.deb \
 && rm *.deb \
 && curl -SL "http://php.net/get/php-$PHP_VERSION.tar.bz2/from/this/mirror" -o php.tar.bz2 \
 && curl -SL "http://php.net/get/php-$PHP_VERSION.tar.bz2.asc/from/this/mirror" -o php.tar.bz2.asc \
 && gpg --verify php.tar.bz2.asc \
 && mkdir -p /usr/src/php \
 && tar -xf php.tar.bz2 -C /usr/src/php --strip-components=1 \
 && rm php.tar.bz2* \
 && cd /usr/src/php \
 && ./buildconf --force \
 && ./configure --disable-cgi \
    $(command -v apxs2 > /dev/null 2>&1 && echo '--with-apxs2' || true) \
    --with-config-file-path="$PHP_INI_DIR" \
    --with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \
    --with-mysql \
    --with-mysqli \
    --with-pdo-mysql \
    --with-openssl=/usr/local/ssl \
    --with-zlib \
    --with-zlib-dir=/lib/x86_64-linux-gnu \
    --enable-fpm \
    --with-fpm-user=www-data \
    --with-fpm-group=www-data \
 && make -j"$(nproc)" \
 && make install \
 && dpkg -r bison libbison-dev \
 && apt-get purge -y --auto-remove autoconf2.13 \
 && make clean

# Install tools
RUN apt-get update \
 && apt-get install -y \
    nginx \
    vim \
    exim4-daemon-light \
    supervisor \
    libjpeg62-turbo-dev \
    php5-memcached \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 && find /var/log -type f | while read f; do echo -ne '' > $f; done;

COPY docker-php/* /usr/local/bin/

# Install Ioncube
RUN wget http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz \
 && tar xvfz ioncube_loaders_lin_x86-64.tar.gz \
 && PHP_VERSION=$(php -r "echo PHP_MAJOR_VERSION.'.'.PHP_MINOR_VERSION;") \
 && PHP_EXT_DIR=$(php-config --extension-dir) \
 && mkdir -p $PHP_EXT_DIR \
 && cp "ioncube/ioncube_loader_lin_${PHP_VERSION}.so" $PHP_EXT_DIR \
 && cp "ioncube/ioncube_loader_lin_${PHP_VERSION}_ts.so" $PHP_EXT_DIR \
 && rm -rf ioncube ioncube_loaders_lin_x86-64.tar.gz

# Create directory for extensions config files
RUN mkdir -p \
    /usr/local/etc/php/conf.d \
    /etc/php

# Configure extensions
RUN docker-php-ext-configure \
  	gd --with-jpeg-dir=/usr/lib/x86_64-linux-gnu

# Install extensions
RUN docker-php-ext-install curl mbstring gd soap calendar xmlrpc xsl

RUN pear channel-discover zenovich.github.io/pear

RUN yes "" | pecl install memcache xdebug-2.2.7 ZendOpcache zenovich/runkit

# Configure PHP
COPY php/php.ini /usr/local/lib
RUN mkdir -p /usr/local/etc/php/conf.d
RUN mv /usr/local/etc/php-fpm.conf.default /etc/php/php-fpm.conf

# Configure exim
COPY exim/set-exim4-update-conf /bin/
RUN chmod a+x /bin/set-exim4-update-conf

# Configure supervisor
COPY supervisor/supervisord-*.conf /etc/supervisor/conf.d/
RUN mkdir -p \
	/var/lock/apache2 \
	/var/run/apache2 \
	/var/log/supervisor

# Configure entrypoints
RUN mkdir -p /entrypoint

COPY entrypoint.sh /entrypoint/entrypoint.sh
COPY exim/entrypoint.sh /entrypoint/exim-entrypoint.sh
COPY php/entrypoint.sh /entrypoint/php-entrypoint.sh

RUN chmod a+x /entrypoint/*.sh

ENTRYPOINT ["/entrypoint/entrypoint.sh"]

WORKDIR /var/www/html

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord-web.conf"]