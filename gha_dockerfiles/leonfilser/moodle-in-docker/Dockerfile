FROM	php:7.4-apache

MAINTAINER Leon Filser <filser@lfi.rwth-aachen.de>

#Some of this will later be overwritten by the docker-compose.yml
ENV	DIR=/var/www/moodle
ENV	VERSION=MOODLE_38_STABLE
ENV	DATADIR=/var/www/moodledata
ENV	AP2USER=www-data:www-data

#Creating the necessary directories
RUN	mkdir ${DIR} ${DATADIR}

#Setting the main directory
WORKDIR	${DIR}

#Variables used to automatically install moodle. The defauls can be overwritten in the docker-compose.yml
ENV	MOODLELANG=de \
	WWWROOT="http://localhost" \
	DBTYPE=mariadb \
	DBHOST=localhost \
	DBNAME=moodle \
	DBUSER=moodle \
	DBPASS=passwd \
	FULLNAME=NewSite \
	SHORTNAME=New \
	ADMINPASS=passwd \
	ADMINMAIL=admin@localhost \
	USESSL=false

#Installs the necessary applications and php modules
RUN	apt-get update && apt-get install --no-install-recommends -y \
	git \
        cron \
	libzip-dev \
	libpng-dev \
	libicu-dev \
	libxml2-dev \
	libxslt1-dev
RUN	docker-php-ext-install \
	zip \
	mysqli \
	gd \
	intl \
	xmlrpc \
	soap \
	opcache \
	xsl

#This is recommended by Moodle. Turns off error messaging for security reasons
RUN	echo "display_errors=0" >> /usr/local/etc/php/conf.d/errors.ini

#Changes the Apache config files
RUN	cd /etc/apache2/sites-available \
	&& sed "s|\/var/www/html|/var/www/moodle|g" 000-default.conf > moodle.conf \
	&& a2ensite moodle.conf \
	&& a2dissite 000-default.conf \
	&& rm 000-default.conf default-ssl.conf \
	&& rm -r /var/www/html

COPY	./entrypoint.sh /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]
