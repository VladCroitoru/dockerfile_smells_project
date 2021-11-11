FROM alpine:latest
MAINTAINER Salisbury Almeida <sbalmeida@bury.com.br>

ENV TZ America/Sao_Paulo
ENV HOSTNAME srvweb.bury.eng.br

RUN apk update \
    && apk upgrade

RUN apk add --no-cache \
    apache2 \
    apache2-proxy \
    apache2-utils \
    apache2-ssl \
    apache2-error \
    apache2-webdav \
    geoip \
    tzdata \
    clamav \
    curl \
    fuse \
    grep \
    git \
    imagemagick \
    mysql-client \
    patch \
    perl \
    python3 \
    rsync \
    unzip \
    zip \
    git-cvs \
    git-svn \
    openjdk7-jre \
    make \
    binutils \
    cifs-utils \
    mailx \
    php7-intl \
    php7-openssl \
    php7-dba \
    php7-sqlite3 \
    php7-pear \
    php7-litespeed \
    php7-pdo_mysql \
    php7-fpm \
    php7-imagick \
    php7-mysqlnd \
    php7-snmp \
    php7-fileinfo \
    php7-mbstring \
    php7-pear-mail_mime \
    php7-xmlrpc \
    php7-xmlreader \
    php7-pear-mdb2_driver_mysql \
    php7-pdo_sqlite \
    php7-exif \
    php7-recode \
    php7-opcache \
    php7-ldap \
    php7-posix \
    php7-session \
    php7-gd \
    php7-gettext \
    php7-mailparse \
    php7-json \
    php7-xml \
    php7 \
    php7-iconv \
    php7-sysvshm \
    php7-curl \
    php7-phar \
    php7-imap \
    php7-pdo_dblib \
    php7-xdebug \
    php7-zip \
    php7-apache2 \
    php7-ctype \
    php7-mcrypt \
    php7-pear-net_smtp \
    php7-bcmath \
    php7-calendar \
    php7-tidy \
    php7-dom \
    php7-sockets \
    php7-memcached \
    php7-soap \
    php7-apcu \
    php7-sysvmsg \
    php7-zlib \
    php7-imagick-dev \
    php7-ftp \
    php7-sysvsem \
    php7-pdo \
    php7-bz2 \
    php7-mysqli \
    php7-simplexml \
    php7-xmlwriter

COPY run.sh /srv/scripts/

ADD http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz /srv/tmp/

RUN tar -C /srv/tmp/ -xzf /srv/tmp/ioncube_loaders_lin_x86-64.tar.gz \
    && cp /srv/tmp/ioncube/ioncube_loader_lin_7.1.so /usr/lib/php7/modules/ \
    && chmod -R 755 /srv/scripts \
    && mkdir /run/apache2 \
    && mkdir /run/php7 \
    && sed -rie 's|ServerName srvweb.bury.eng.br:80|ServerName ${HOSTNAME}:80|g' /etc/apache2/httpd.conf \
    && echo '127.0.0.1 ${HOSTNAME}' >> /etc/hosts

RUN mkdir /var/www/vhosts \
    && rm /var/www/localhost/htdocs/* \
    && echo '<?php phpinfo(); ?>' > /var/www/localhost/htdocs/info.php \
    && chown -R apache:apache /var/www/localhost/htdocs

COPY ./apache2/httpd.conf /etc/apache2/httpd.conf
COPY ./apache2/conf.d/* /etc/apache2/conf.d/

COPY ./php7/php-fpm.d/* /etc/php7/php-fpm.d/
COPY ./php7/php-fpm.conf /etc/php7/php-fpm.conf
COPY ./php7/php.ini /etc/php7/php.ini

COPY ./apache2_error/*.html /usr/share/apache2/error/
COPY ./apache2_error/*.ico /usr/share/apache2/error/
COPY ./apache2_error/logo_small.png /usr/share/apache2/error/logo_small.png
COPY ./apache2_error/icons/* /usr/share/apache2/error/icons/

RUN rm -R /srv/tmp/*

EXPOSE 80 443

VOLUME ["/var/log", "/etc/php7", "/etc/apache2", "/var/www"]

CMD ["/srv/scripts/run.sh"]
