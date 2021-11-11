FROM php:7.0-apache

RUN apt-get update&&apt-get install mc nano wget  -y
RUN rm -rf /var/www/html
RUN cd /var/www/html/ && \
	 touch info.php && \
echo "<?php phpinfo(); ?>" > info.php
COPY kijelzo /var/www/html
RUN chmod 755 -R  /var/www/html
RUN /usr/sbin/apachectl start
EXPOSE 80 443

