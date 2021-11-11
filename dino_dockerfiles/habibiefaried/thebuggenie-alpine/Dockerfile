FROM alpine:edge

MAINTAINER habibiefaried@gmail.com
#Default Config, just change this
ENV MYSQL_ROOT_PASSWORD=thebuggenie
ENV GENIE_DB=thebuggenie

RUN apk upgrade --no-cache --update && apk add --no-cache --update \
        bash \
        ca-certificates \
        libuuid \
        apr \
        apr-util \
        libjpeg-turbo \
        icu \
        icu-libs \
        pcre \
        zlib zlib-dev \
        libxml2 libxml2-dev \
        git mysql mysql-client nano \
        php5-apache2 apache2 apache2-ssl apache2-proxy-html apache2-http2 apache2-dev apache2-utils apache2-proxy \
		php5-mcrypt \
		php5-soap \
		php5-openssl \
		php5-gmp \
		php5-pdo_odbc \
		php5-json \
		php5-dom \
		php5-pdo \
		php5-zip \
		php5-mysql \
        php5-mysqli \
		php5-sqlite3 \
		php5-apcu \
		php5-intl \
		php5-imagick \
		php5-pdo_pgsql \
		php5-pgsql \
		php5-bcmath \
		php5-gd \
		php5-xcache \
		php5-mcrypt \
		php5-ldap \
		php5-odbc \
		php5-pdo_mysql \
		php5-pdo_sqlite \
		php5-gettext \
		php5-xmlreader \
		php5-xmlrpc \
		php5-bz2 \
		php5-memcache \
		php5-mssql \
		php5-iconv \
		php5-pdo_dblib \
		php5-curl \
		php5-ctype \
		php5-dev \  
		php5-common \
		php5-pear \
		php5-xml \
		php5-wddx \
		php5-xsl \
		php5-ftp \
		php5-phar \
		php5-posix \
		php5-shmop \
		php5-soap \
		php5-sockets \
		php5-sqlite3 \
		php5-zlib \
		php5-phpmailer \
		php5-zip \
		php5-exif \
		php5-phpdbg \
		php5-opcache \
	&& mkdir /run/apache2 \
    && sed -i 's/#LoadModule\ rewrite_module/LoadModule\ rewrite_module/' /etc/apache2/httpd.conf \
    && sed -i 's/#LoadModule\ slotmem_shm_module/LoadModule\ slotmem_shm_module/' /etc/apache2/httpd.conf \
    && sed -i 's/DirectoryIndex\ index.html/DirectoryIndex\ index.php\ index.html/' /etc/apache2/httpd.conf \
    && mkdir -p /opt/utils

RUN apk add --no-cache bash build-base wget curl m4 autoconf libtool imagemagick imagemagick-dev zlib zlib-dev libcurl curl-dev libevent libevent-dev libidn libmemcached libmemcached-dev libidn-dev && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY my.cnf /etc/mysql/my.cnf
RUN echo "export TERM=xterm" > /root/.bashrc
RUN echo 'PS1="\[\033[35m\]\t\[\033[m\]-\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "' >> /root/.bashrc
VOLUME ["/app"]
WORKDIR /root

COPY init.sh /init.sh
RUN chmod +x /init.sh
RUN echo 'DocumentRoot "/var/www/localhost/htdocs/public"' >> /etc/apache2/httpd.conf
RUN printf "\n<Directory \"/var/www/localhost/htdocs/public\">\n\tDirectoryIndex index.php index.html\n\tAllowOverride All\n</Directory>\n" >> /etc/apache2/httpd.conf

WORKDIR /var/www/localhost
RUN rm -rf htdocs && git clone https://github.com/thebuggenie/thebuggenie.git htdocs 
WORKDIR /var/www/localhost/htdocs

##I'm using master version of buggenie
RUN composer install && mkdir cache && chmod -R 777 cache
RUN chown -R apache:apache /var/www/localhost/htdocs/
RUN chmod a+w /var/www/localhost/htdocs/ && chmod a+w /var/www/localhost/htdocs/public/  && touch /var/www/localhost/htdocs/core/config/b2db.yml && chmod a+w /var/www/localhost/htdocs/core/config/b2db.yml
RUN sed -i 's~UTF-8//IGNORE~UTF-8~' /var/www/localhost/htdocs/core/framework/Action.php

CMD ["/init.sh"]