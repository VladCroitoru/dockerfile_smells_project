# conferencetitle.zvan.net
FROM php:7.0-apache
MAINTAINER ben@zvan.net
RUN apt-get update && \
	ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load
COPY  src/main/webapp/ /var/www/html/ 
