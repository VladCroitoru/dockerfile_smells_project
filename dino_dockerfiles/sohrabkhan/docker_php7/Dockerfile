FROM php:7.0-apache
MAINTAINER Sohrab Khan <sohrab@sohrabkhan.com>

# Install IonCube Loader
RUN apt-get update && apt-get upgrade -yqq
RUN apt-get install -y wget
#RUN wget http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
#RUN tar zxvf ioncube_loaders_lin_x86-64.tar.gz
#RUN mv ioncube/ioncube_loader_lin_5.6.so /usr/local/lib/php/extensions/no-debug-non-zts-20131226/
#RUN touch /usr/local/etc/php/conf.d/ioncube.ini && echo "zend_extension=ioncube_loader_lin_5.6.so" >> /usr/local/etc/php/conf.d/ioncube.ini

# Install Sass
RUN apt-get install -y rubygems
RUN su -c "gem install sass"


RUN docker-php-ext-install -j$(nproc) mysqli pdo pdo_mysql mbstring
RUN a2enmod rewrite
ADD . /var/www/html/

#RUN composer install

EXPOSE 80