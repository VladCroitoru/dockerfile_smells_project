FROM ahmet2mir/debian:wheezy
MAINTAINER Ahmet Demir <ahmet2mir+github@gmail.com>

ENV RELEASE wheezy
ENV DEBIAN_FRONTEND noninteractive
ENV SHELL /bin/bash

# Curl extension
RUN apt-get update && apt-get install -y nginx php5-fpm php5-curl php5-pgsql php5-mysql

# Adding files
ADD . /docker

RUN mkdir -p /webapps/rainloop /webapps/logs/rainloop && \
	cd /tmp && \
	curl -R -L -O "http://repository.rainloop.net/v2/webmail/rainloop-latest.zip" && \
	unzip rainloop-latest.zip -d /webapps/rainloop && \
	find /webapps/rainloop -type d -exec chmod 755 {} \; && \
	find /webapps/rainloop -type f -exec chmod 644 {} \; && \
	chown -R www-data:www-data /webapps/rainloop && \
	cp -f /docker/assets/conf/nginx.conf /etc/nginx/nginx.conf &&  \
	cp -f /docker/assets/conf/nginx-rainloop.conf /etc/nginx/sites-available/rainloop.conf &&  \
	ln -s /etc/nginx/sites-available/rainloop.conf /etc/nginx/sites-enabled/rainloop.conf && \
	sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php5/fpm/php-fpm.conf

# "Configure services"
# Based on https://github.com/mingfang/docker-salt
RUN for dir in /docker/services/*;\
    do echo $dir; chmod +x $dir/run $dir/log/run;\
    ln -sf $dir /etc/service/; done

# Expose services
EXPOSE 22 80

