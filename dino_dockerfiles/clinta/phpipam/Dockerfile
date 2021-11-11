FROM php:7.2-apache
MAINTAINER Clint Armstrong <clint@clintarmstrong.net>

# Install required deb packages
RUN apt-get update && \ 
	apt-get install -y git libgmp-dev libmcrypt-dev libfreetype6-dev libjpeg62-turbo-dev libldb-dev libldap2-dev && \
	ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so && \
	ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so && \
	rm -rf /var/lib/apt/lists/* && \
	docker-php-ext-configure mysqli --with-mysqli=mysqlnd && \
	ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h && \
	docker-php-ext-configure gmp --with-gmp=/usr/include/x86_64-linux-gnu && \
	docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
	docker-php-ext-install -j$(nproc) pdo_mysql sockets gd gmp ldap gettext pcntl && \
	echo ". /etc/environment" >> /etc/apache2/envvars && \
	a2enmod rewrite

ENV PHPIPAM_SOURCE="https://github.com/phpipam/phpipam/archive/" \
    PHPIPAM_VERSION="1.3.2" \
    MYSQL_HOST="mysql" \
    MYSQL_USER="phpipam" \
    MYSQL_PASSWORD="phpipamadmin" \
    MYSQL_DB="phpipam" \
    MYSQL_PORT="3306" \
    SSL="false" \
    SSL_KEY="/path/to/cert.key" \
    SSL_CERT="/path/to/cert.crt" \
    SSL_CA="/path/to/ca.crt" \
    SSL_CAPATH="/path/to/ca_certs" \
    SSL_CIPHER="DHE-RSA-AES256-SHA:AES128-SHA"

COPY php.ini /usr/local/etc/php/

# copy phpipam sources to web dir
ADD ${PHPIPAM_SOURCE}/${PHPIPAM_VERSION}.tar.gz /tmp/
RUN tar -xzf /tmp/${PHPIPAM_VERSION}.tar.gz -C /var/www/html/ --strip-components=1 && \
    cp /var/www/html/config.dist.php /var/www/html/config.php

# Use system environment variables into config.php
RUN sed -i \ 
    -e "s/\['host'\] = 'localhost'/\['host'\] = getenv(\"MYSQL_HOST\")/" \ 
    -e "s/\['user'\] = 'phpipam'/\['user'\] = getenv(\"MYSQL_USER\")/" \ 
    -e "s/\['pass'\] = 'phpipamadmin'/\['pass'\] = getenv(\"MYSQL_PASSWORD\")/" \ 
    -e "s/\['name'\] = 'phpipam'/\['name'\] = getenv(\"MYSQL_DB\")/" \ 
    -e "s/\['port'\] = 3306/\['port'\] = getenv(\"MYSQL_PORT\")/" \ 
    -e "s/\['ssl'\] *= false/\['ssl'\] = getenv(\"SSL\")/" \ 
    -e "s/\['ssl_key'\] *= '\/path\/to\/cert.key'/['ssl_key'\] = getenv(\"SSL_KEY\")/" \ 
    -e "s/\['ssl_cert'\] *= '\/path\/to\/cert.crt'/['ssl_cert'\] = getenv(\"SSL_CERT\")/" \ 
    -e "s/\['ssl_ca'\] *= '\/path\/to\/ca.crt'/['ssl_ca'\] = getenv(\"SSL_CA\")/" \ 
    -e "s/\['ssl_capath'\] *= '\/path\/to\/ca_certs'/['ssl_capath'\] = getenv(\"SSL_CAPATH\")/" \ 
    -e "s/\['ssl_cipher'\] *= 'DHE-RSA-AES256-SHA:AES128-SHA'/['ssl_cipher'\] = getenv(\"SSL_CIPHER\")/" \ 
    /var/www/html/config.php

EXPOSE 80
