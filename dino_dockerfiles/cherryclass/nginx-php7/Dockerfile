FROM nginx:1.13.0

MAINTAINER Luc Frébourg

ENV DEBIAN_FRONTEND noninteractive

#install stuff
RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q && apt-get -y -q autoclean && apt-get -y -q autoremove)
RUN apt-get install --no-install-recommends --no-install-suggests -y \
	apt-utils \
	php7.0-fpm \
    	php-mysql \
	php-xml \
	php7.0-mbstring \
	php-gd \
	sudo \
	nano \
   	ssh 
	
RUN mkdir /home/site
RUN mkdir /home/site/www
ADD index.php /home/site/www/index.php
RUN chown -R www-data:www-data /home/site/www
RUN chsh -s /bin/bash www-data

#CONFIG ----------------------
#PHP
ADD php.ini /etc/php/7.0/fpm/php.ini
#ADD fastcgi_params /etc/nginx/fastcgi_params
#ADD www.conf /etc/php/7.0/fpm/pool.d/www.conf
#ADD php-fpm.conf /etc/php/7.0/fpm/php-fpm.conf

#NGINX
ADD nginx.conf /etc/nginx/nginx.conf
ADD default.conf /etc/nginx/conf.d/default.conf
ADD wordpress.conf /etc/nginx/wordpress.conf
ADD phpfpm.conf /etc/nginx/phpfpm.conf

#start services
CMD service php7.0-fpm start && nginx -g "daemon off;"

#on bluemix, you need to put -P or create container with web console.
EXPOSE 80 443 22 25
