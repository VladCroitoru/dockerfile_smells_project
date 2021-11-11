# dolia/nginx-php
#
# VERSION       1.0

# use the ubuntu base image provided by dotCloud
FROM richarvey/nginx-php-fpm

#fix os x boot2docker mount staff bug

RUN usermod -u 1000 www-data 

RUN apt-get update

#encoding 

RUN export LESSCHARSET=utf-8

#replace vim 

RUN apt-get install -y vim 

# set timezone
RUN echo "Asia/Shanghai">/etc/timezone&&dpkg-reconfigure tzdata

# enable php  mcrypt
RUN php5enmod mcrypt

#install curl 

RUN apt-get install -y curl

# install nodejs

RUN apt-get install -y nodejs

# node link to nodejs

RUN ln -s /usr/bin/nodejs /usr/bin/node

# install npm

RUN curl -L https://npmjs.org/install.sh | sh

# install grunt 

RUN npm install -g grunt-cli

# install gulpjs

RUN npm install -g gulp

# install bower

RUN npm install -g bower


# install php composer

RUN php -r "readfile('https://getcomposer.org/installer');" | php

RUN mv composer.phar /usr/local/bin/composer


#install beantalkd

RUN apt-get -y install beanstalkd

RUN  sed -i   '$a [program:beanstalkd]\ncommand=/usr/bin/beanstalkd -l 127.0.0.1 -p 11300\nautorestart=true\nstdout_events_enabled=true\nstderr_events_enabled=true'  /etc/supervisord.conf 
CMD /start.sh
