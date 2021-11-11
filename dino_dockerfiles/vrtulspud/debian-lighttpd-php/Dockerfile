FROM vrtulspud/debian-lighttpd:1.0
MAINTAINER vrtulspud <email@domain.com>

# install lighttpd and PHP
RUN apt-get update && apt-get -y install \
	php5-cgi \
	php5-gd \
	wget \
&& apt-get clean autoclean \
&& apt-get autoremove \
&& lighttpd-enable-mod cgi \
&& lighttpd-enable-mod fastcgi \
&& rm -rf /var/lib/{apt,dpkg,cache,log}

# configure PHP with lighttpd
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/cgi/php.ini
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
COPY cgi.conf /etc/lighttpd/conf.d/cgi.conf
COPY php.ini /etc/php/php.ini

EXPOSE 80

# start lighttpd
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]

