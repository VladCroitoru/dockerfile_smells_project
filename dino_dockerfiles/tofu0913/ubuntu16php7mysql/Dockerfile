FROM ubuntu:16.04
MAINTAINER Cliff Chen<tofu0913 (at) gmail (dot) com>

RUN apt-get update 
RUN apt-get -y install wget net-tools curl apt-transport-https
RUN apt-get -y install php7.0 libapache2-mod-php7.0 mcrypt php7.0-mcrypt php-mbstring php-pear php7.0-dev apache2 php7.0-mysql php7.0-gd php7.0-curl php7.0-zip 
#RUN source ~/.bashrc
RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8
RUN a2enmod ssl
ADD default-ssl.conf /etc/apache2/sites-available/
RUN a2ensite default-ssl.conf
ADD php.ini /etc/php/7.0/apache2/php.ini

EXPOSE 80

CMD service apache2 start && tail -F /var/log/apache2/error.log
