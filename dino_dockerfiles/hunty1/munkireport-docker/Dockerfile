# Dockerfile for MunkiReport-PHP
# This docker image will take environmental variables
# in order to send data to an external MySQL database
# simply provide the db name, username, password and server address

# Version 0.8 - 02-11-2015
# MR-PHP Version 2.6.0 (October 20, 2015)

FROM debian:jessie

MAINTAINER Calum Hunter <calum.h@gmail.com>

# The version of Munki report to download
ENV MR_VERS v2.6.0.tar.gz

# Set Environmental variables
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm
ENV TZ Australia/Sydney

# The version of Munki report to download
# Master Branch

# Set Env variables for Munki Report Config
ENV DB_NAME munkireport
ENV DB_USER admin
ENV DB_PASS password
ENV DB_SERVER sql.test.internal
ENV MR_SITENAME MunkiReport
ENV MR_TIMEZONE Australia/Sydney

# Define proxy setting variables for Munki report
# set this to mod1, mod2 or no depending upon your proxy server needs. See the Readme for more info.
ENV proxy_required no
ENV proxy_server proxy.example.com
ENV proxy_uname proxyuser
ENV proxy_pword proxypassword
ENV proxy_port 8080

# Install base packages for MR
RUN apt-get update && \
	apt-get -y install \
	nginx \
	nano \
	curl \
	php5-fpm \
	php5-mysql \
	php5-ldap && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# Make folder for enabled sites in nginx
# Add line to php config to prevent blank page, fix PHP CGI pathinfo
RUN mkdir -p /www/munkireport && \
	mkdir -p /etc/nginx/sites-enabled/ && \
	rm -rf /etc/nginx/sites-enabled/* && \
	rm -rf /etc/nginx/nginx.conf && \
	sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php5/fpm/php.ini

# Grab our Munki Report Release defined in MR_VERS from Github, unpack it and remove the tarball
ADD https://github.com/munkireport/munkireport-php/archive/$MR_VERS /www/munkireport/$MR_VERS
RUN tar -zxvf /www/munkireport/$MR_VERS --strip-components=1 -C /www/munkireport && \
	rm /www/munkireport/$MR_VERS

# Add our config.php file and nginx configs
ADD config.php /www/munkireport/config.php
ADD munki-report.conf /etc/nginx/sites-enabled/munki-report.conf
ADD nginx.conf /etc/nginx/nginx.conf

# Set up logs to output to stout and stderr
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
	ln -sf /dev/stderr /var/log/nginx/error.log

# Add our startup script
ADD start.sh /start.sh
RUN chmod +x /start.sh

# Expose Ports
EXPOSE 80 443

# Run our startup script
CMD ["/start.sh"]