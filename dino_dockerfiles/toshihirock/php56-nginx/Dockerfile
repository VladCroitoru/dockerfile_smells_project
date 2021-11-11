FROM ubuntu:14.04

ENV LANG=C.UTF-8

MAINTAINER toshihirock

# Setup
RUN apt-get update
RUN apt-get install wget -y
RUN apt-get install software-properties-common python-software-properties -y
RUN add-apt-repository ppa:ondrej/php5-5.6 -y
RUN add-apt-repository ppa:nginx/stable -y
RUN apt-get update

# Install PHP5.6 and latest nginx
RUN apt-get install php5 php5-fpm -y
RUN apt-get install nginx -y

# setting PHP and nginx
COPY conf/default /etc/nginx/sites-available/default 
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN echo "<?php phpinfo(); ?>" > /var/www/index.php

EXPOSE 80

CMD service php5-fpm start && nginx
