FROM php:5.6-apache
MAINTAINER Volker Wiegand <volker.wiegand@cvw.de>

RUN apt-get update && apt-get install -y \
	git \
	libcurl4-openssl-dev \
	libfreetype6-dev \
	libicu-dev \
	libmcrypt-dev \
	vim-tiny \
	&& rm -rf /var/lib/apt/lists/* /var/www/html/index.html

RUN docker-php-ext-install intl mbstring mcrypt mysql

RUN git clone https://github.com/deliciousbrains/sqlbuddy.git /tmp/sqlbuddy_git \
	&& mkdir /var/lib/sqlbuddy \
	&& mv -v /tmp/sqlbuddy_git/src/* /var/lib/sqlbuddy/ \
	&& rm -rf /tmp/sqlbuddy_git /var/www/html/index.html

RUN sed -i -e "/DefaultHost/s/localhost/db/" /var/lib/sqlbuddy/config.php

ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80
