
FROM ubuntu:14.04
MAINTAINER Cameron Morris - camarox53@gmail.com
RUN apt-get -y update 
RUN apt-get install -y apache2 
RUN apt-get -y clean

ENV VIRTUAL_DOMAIN camarox53.com
ENV VIRTUAL_PORT 80
ENV DOCKER_RUN docker run -d -e VIRTUAL_DOMAIN=camarox53.com -v /var/www/${1}:/var/www/html camarox53/docker-apache2
ENV DOCKER_BUILD docker build -t camarox53/docker-apache2 git://github.com/camarox53/docker-apache2
ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_PID_FILE $APACHE_RUN_DIR/apache2.pid
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV LANG C

RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR
EXPOSE 80
CMD ["apache2", "-DFOREGROUND"]
