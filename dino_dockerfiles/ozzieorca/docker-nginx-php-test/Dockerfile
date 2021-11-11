FROM ubuntu
MAINTAINER Scotty Waggoner <ozzieorca@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu/ precise universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y curl wget
RUN apt-get install -y software-properties-common python-software-properties
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN add-apt-repository -y ppa:ondrej/php5
RUN apt-get update

RUN apt-get install -y nginx
RUN apt-get install -y php5-fpm
RUN apt-get install -y php5-cli php5-mysql php5-intl php-apc php5-imap php5-mcrypt php5-curl php5-gd php5-json

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini

RUN rm /etc/nginx/sites-enabled/default
ADD daviscru.conf /etc/nginx/sites-available/daviscru.conf
RUN ln -s /etc/nginx/sites-available/daviscru.conf /etc/nginx/sites-enabled/daviscru.conf
ADD daviscru-php.ini /etc/php5/fpm/conf.d/daviscru-php.ini

ADD . /var/www/daviscru

EXPOSE 80

CMD php5-fpm && nginx

#docker run -i -t -p 80:80 -v /vagrant:/var/www/daviscru ozzieorca/daviscru /bin/bash
#docker run -d -p 80:80 -v /vagrant:/var/www/daviscru ozzieorca/daviscru
#docker build -t ozzieorca/daviscru /vagrant/server/nginx+php

#docker run -d -p 80:80 ozzieorca/docker-nginx-php-test
