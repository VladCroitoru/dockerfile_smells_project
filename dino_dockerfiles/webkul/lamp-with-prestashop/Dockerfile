From ubuntu:14.04

MAINTAINER Prashant Arora <prashant089@webkul.com>

RUN apt-get -y update

RUN apt-get -y install lamp-server^

RUN mkdir -p /var/lock/apache2 /var/run/apache2

RUN apt-get install -y wget unzip vim nano gedit

RUN apt-get install libapache2-mod-php5 php5-mcrypt php5-gd

RUN php5enmod mcrypt

RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

RUN apt-get install -y openssh-server

RUN mkdir -p /var/run/sshd

RUN apt-get install -y supervisor

RUN mkdir -p /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY mysql.sh /etc/mysql.sh

RUN chmod +x /etc/mysql.sh

COPY prestashop.zip /var/www/html/

RUN cd /var/www/html && unzip prestashop.zip 

RUN rm -rf /var/www/html/prestashop.zip

RUN rm /var/www/html/index.html

COPY adminer.php /var/www/html/prestashop/

RUN cd /var/www/html && chown -R www-data: prestashop

EXPOSE 80

EXPOSE 22

EXPOSE 3306

CMD ["/usr/bin/supervisord"]
