FROM ubuntu:14.04

RUN echo "deb http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu trusty main" >> /etc/apt/sources.list
RUN echo "deb-src http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu trusty main" >> /etc/apt/sources.list

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 314DF160
RUN apt-get update

# install apache
RUN apt-get install -y apache2 apache2-mpm-worker apache2-threaded-dev apache2-utils
#libapache2-mod-fastcgi
RUN a2enmod actions cgi alias
RUN apt-get install -y libapache2-mod-php5 php5-common php5-cli php5-fpm php5

# prerequisites
RUN apt-get install -y php5-gd gdal-bin tilecache postgis

# mapserver
RUN apt-get install -y mapserver-bin cgi-mapserver php5-mapscript

#RUN echo "extension=php_mapscript.so" >> /etc/php5/apache2/php.ini

CMD ["apachectl", "-D", "FOREGROUND"]

EXPOSE 22 80 443
