FROM ubuntu:16.04

MAINTAINER  Suilong Liang <suilong.liang@worktogether.io>

ENV PHP_MAJOR 7.1
ENV PHP_VERSION 7.1.15
ENV PHP_VERSION_MINOR 1+ubuntu16.04.1+deb.sury.org+2
ENV LC_ALL C.UTF-8

# Manually Add Ondrej PHP PPA https://launchpad.net/~ondrej/+archive/ubuntu/php
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 14AA40EC0831756756D7F66C4F4EA0AAE5267A6C
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" > /etc/apt/sources.list.d/php.list

RUN apt-get -y update && \
    apt-get -y -V install php${PHP_MAJOR}-fpm \
	php${PHP_MAJOR}-cli=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php${PHP_MAJOR}-curl=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php${PHP_MAJOR}-gd=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php${PHP_MAJOR}-intl=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php-xdebug \ 
	php${PHP_MAJOR}-mbstring=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php${PHP_MAJOR}-mcrypt=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php${PHP_MAJOR}-mysql=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php${PHP_MAJOR}-xml=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php${PHP_MAJOR}-soap=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php${PHP_MAJOR}-xsl=${PHP_VERSION}-${PHP_VERSION_MINOR} \
	php${PHP_MAJOR}-zip=${PHP_VERSION}-${PHP_VERSION_MINOR} && \
    rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

RUN mkdir -p /run/php/

VOLUME /var/www/html/ /etc/php/${PHP_MAJOR}/fpm/

EXPOSE 9000

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["start"]
