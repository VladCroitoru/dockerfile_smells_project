FROM phusion/baseimage:latest
MAINTAINER Stefan Siegl <stesie@brokenpipe.de>

RUN apt-get update && \
	apt-get -y install libmozjs-24-dev git php5-dev && \
	apt-get clean

RUN git clone https://github.com/christopherobin/php-spidermonkey.git /usr/local/src/php-spidermonkey

RUN cd /usr/local/src/php-spidermonkey && \
	phpize && \
	./configure && \
	make && \
	make install

RUN echo extension=spidermonkey.so >> /etc/php5/cli/conf.d/20-spidermonkey.ini

CMD php5 -a
