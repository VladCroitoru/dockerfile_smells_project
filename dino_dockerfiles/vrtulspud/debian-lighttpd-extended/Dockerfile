FROM vrtulspud/debian-lighttpd-php:1.0
MAINTAINER vrtulspud <email@domain.com>

# install lighttpd and PHP
RUN apt-get update && apt-get -y install \
	imagemagick \
&& apt-get clean autoclean \
&& apt-get autoremove \
&& rm -rf /var/lib/{apt,dpkg,cache,log}

EXPOSE 80

# start lighttpd
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]

