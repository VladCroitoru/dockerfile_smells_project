FROM phusion/baseimage:0.9.17
MAINTAINER pressrelations
EXPOSE 80 8500
VOLUME ["/var/www", "/tmp/config"]

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y wget unzip xsltproc apache2 php5 libapache2-mod-php5 php5-mcrypt php5-gd pngcrush gifsicle
RUN apt-get install -y imagemagick --fix-missing
#apache rewrite
RUN php5enmod mcrypt
RUN a2enmod rewrite
ADD ./build/install/ /tmp/
ADD ./build/service/ /etc/service/
ADD ./build/my_init.d/ /etc/my_init.d/
RUN /tmp/install-cf11.sh
ADD ./build/apache2/sites-enabled/ /etc/apache2/sites-enabled-cms/
RUN cp /etc/apache2/sites-enabled-cms/*.conf /etc/apache2/sites-enabled/
