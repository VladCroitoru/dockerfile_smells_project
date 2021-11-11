FROM debian:jessie
MAINTAINER "Gary Smith" <docker@kc.gs>

RUN apt-get update && apt-get install -y \
	freetds-common \
	freetds-bin \
	tdsodbc \
	unixodbc-dev \
 	# && set -x \
  #   && cd /usr/src/php/ext/odbc \
  #   && phpize \
  #   && sed -ri 's@^ *test +"\$PHP_.*" *= *"no" *&& *PHP_.*=yes *$@#&@g' configure \
  #   && ./configure --with-unixODBC=shared,/usr \
    && docker-php-ext-install odbc

RUN service apache2 restart

