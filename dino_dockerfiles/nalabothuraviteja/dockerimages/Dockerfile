FROM ubuntu
MAINTAINER rt
RUN apt-get update
RUN apt-get install apache2 -y
EXPOSE 80
CMD apachectl -f /etc/apache2/apache2.conf -e info -DFOREGROUND
