FROM ubuntu:trusty

MAINTAINER wuwenbin <wenbin.wu@foxmail.com>

ADD sources.list /etc/apt/

RUN apt-get update

RUN apt-get install -y sudo wget unzip mysql-server nginx php5-fpm php5-mysql

RUN service mysql start \
 && mysqladmin create zentao

RUN mkdir /var/www \
 && cd /var/www \
 && wget -O zentaopms.zip http://dl.cnezsoft.com/zentao/7.2.5/ZenTaoPMS.7.2.5.zip \
 && unzip zentaopms.zip

RUN rm -Rf /etc/nginx/sites-enabled/*

ADD zentaopms.conf /etc/nginx/sites-enabled/

ADD run.sh /

RUN chmod +x /run.sh

CMD /run.sh

