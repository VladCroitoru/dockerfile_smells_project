FROM php:5.6-apache
MAINTAINER Tuschl <tuschl@digitalmobil.com>

# Enable Apache Rewrite Module
RUN a2enmod rewrite

RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \
	wget \
	libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng12-dev \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
				       
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) gd

RUN echo 'date.timezone="Europe/Berlin"' > /usr/local/etc/php/conf.d/php-timezone.ini

ENV COCKPIT_VERSION=master
ENV COCKPIT_ROOT=/var/www/html

ADD https://github.com/COCOPi/cockpit/archive/$COCKPIT_VERSION.tar.gz /usr/src/cockpit.tar.gz
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["apache2-foreground"]
