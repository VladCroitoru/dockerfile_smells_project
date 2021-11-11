FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install -y software-properties-common apt-utils pkg-config
RUN add-apt-repository -y ppa:ondrej/php
RUN apt-get update -y

#PHP 7 deps
RUN apt-get install -y --allow-unauthenticated \
	libcurl4-openssl-dev libmcrypt-dev libzip-dev libxml2-dev libjpeg-dev libxpm-dev \
	libxslt-dev libpq-dev sqlite3 libsqlite3-dev libbz2-dev libpng-dev libfreetype6-dev \
	libc-client2007e-dev libicu-dev git ssh subversion sudo reprepro git libmemcached-dev \
	libmemcached11

#PHP 7
RUN apt-get install -y --allow-unauthenticated php7.0 php7.0-dev \
	php7.0-mysql php7.0-curl php7.0-mbstring php7.0-mcrypt php7.0-soap php7.0-xml php7.0-xsl \
	php7.0-zip php7.0-bz2 php7.0-sqlite3 php7.0-pgsql php7.0-opcache php7.0-bcmath php7.0-json \
	php7.0-gd php7.0-intl php7.0-ldap php7.0-apcu

#PHP 7 Memcached
WORKDIR /tmp/
RUN git clone https://github.com/php-memcached-dev/php-memcached
WORKDIR /tmp/php-memcached
RUN git checkout -b php7 origin/php7
RUN phpize
RUN ./configure
RUN make
RUN make install
RUN echo "extension=memcached.so" > "/etc/php/7.0/mods-available/memcached.ini"
RUN ln -s /etc/php/7.0/mods-available/memcached.ini /etc/php/7.0/apache2/conf.d/20-memcached.ini
WORKDIR /home/
RUN rm -Rf /tmp/php-memcached

#Apache2
RUN apt-get install -y apache2 libapache2-modsecurity
RUN a2enmod rewrite
RUN mv /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
RUN . /etc/apache2/envvars

#Misc
ADD sudoers /etc/sudoers
ADD site.conf /etc/apache2/sites-enabled/000-default.conf
ADD php.ini /etc/php/7.0/apache2/php.ini

RUN wget https://raw.githubusercontent.com/docker-library/php/master/7.0/apache/apache2-foreground && \
		mv apache2-foreground /usr/sbin/apache2-foreground && \
		chmod +x /usr/sbin/apache2-foreground

RUN wget http://pecl.php.net/get/APCu -O apcu.tar.gz && \
 		tar zvfx apcu.tar.gz && \
		mv apcu*/apc.php /var/www/apc.php && \
		rm -r apcu*/


VOLUME ["/var/log/apache2/", "/var/www/html/"]

EXPOSE 80
CMD ["/usr/sbin/apache2-foreground"]
