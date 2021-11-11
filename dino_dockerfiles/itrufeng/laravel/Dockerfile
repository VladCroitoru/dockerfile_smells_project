FROM debian

# update
ADD ./etc/apt/sources.list /etc/apt/sources.list
RUN apt-get -y update

# openssl
RUN apt-get -y install openssl

# mysql
RUN echo mysql-server mysql-server/root_password password root | debconf-set-selections \
  && echo mysql-server mysql-server/root_password_again password root | debconf-set-selections \
  && apt-get -y install mysql-server \
  && service mysql start
EXPOSE 3306

# postgres
RUN apt-get -y install postgresql
EXPOSE 5432

# sqlite3
RUN apt-get -y install sqlite3

# redis
RUN apt-get -y install redis-server

# nodejs
RUN apt-get -y install nodejs \
  && apt-get -y install npm \
  && npm install pm2 -g \
  && npm install bower -g \
  && npm install grunt -g \
  && npm install gulp -g

# beanstalkd
RUN apt-get -y install beanstalkd

# php
RUN apt-get -y install php5 \
  && apt-get -y install php5-fpm \
  && apt-get -y install php5-gd \
  && apt-get -y install php5-sqlite \
  && apt-get -y install php5-redis

# composer
RUN apt-get -y install curl \
  && curl -sS https://getcomposer.org/installer | php \
  && mv composer.phar /usr/local/bin/composer \
  && composer config -g repositories.packagist composer http://packagist.phpcomposer.com

# Laravel Envoy
#RUN composer global require "laravel/envoy=~1.0"

# nginx
RUN apt-get -y install nginx
ADD ./etc/nginx/nginx.conf /etc/nginx/nginx.conf
ADD ./etc/nginx/sites-available/default /etc/nginx/sites-available/default
EXPOSE 80

# Laravel
RUN cd /var/www \
  && composer create-project laravel/laravel --prefer-dist \
  && chown -R www-data ./

# clearn
RUN apt-get -y autoremove \
  && apt-get clean \
  && apt-get autoclean

# user
RUN usermod -u 1000 www-data

ADD ./start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
