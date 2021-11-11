FROM ubuntu:16.04
MAINTAINER rchrdhorne1@gmail.com
RUN apt-get -q update && apt-get -yq dist-upgrade
RUN apt-get -yq install apache2
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/run/apache
ENV PACHE_PID_FILE /var/run/apache/http.pid
ENV TEST_TO_TRIGGER_BUILD 4-8-2016:851
RUN mkdir /run/apache
ADD index.html /var/www/html/index.html
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-DFOREGROUND"]
