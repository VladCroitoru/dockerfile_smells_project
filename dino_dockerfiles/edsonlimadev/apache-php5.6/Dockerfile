FROM ubuntu:latest
MAINTAINER Edson Lima <dddwebdeveloper@gmail.com>

RUN apt-get update
RUN apt-get install -y apache2
RUN echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main" > /etc/apt/sources.list.d/ondrej-php5-5_6-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN apt-get update
RUN apt-get install -y php5
RUN a2enmod rewrite
RUN a2enmod php5
ADD start.sh /bootstrap.sh
RUN chmod 755 /bootstrap.sh

EXPOSE 80
CMD ["/bootstrap.sh"]
