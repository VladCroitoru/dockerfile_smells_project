FROM ubuntu:14.04

MAINTAINER "Philip Bower" <pabower@gmail.com>

WORKDIR /tmp

RUN apt-get update -y && \
	apt-get install -y curl git php5-cli php5-mcrypt php5-gd && \
	curl -sS https://getcomposer.org/installer | php && \
	mv composer.phar /usr/local/bin/composer && \
	apt-get remove --purge curl -y && \
	apt-get clean

RUN php5enmod mcrypt
RUN mkdir -p /data/www

VOLUME ["/data"]
WORKDIR /data/www

ENTRYPOINT ["composer"]
CMD ["--help"]