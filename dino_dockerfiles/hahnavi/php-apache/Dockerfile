FROM ubuntu:14.04

MAINTAINER Abdul M. Hanafi <amunifhanafi@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

#RUN sed -i 's/archive.ubuntu.com/kambing.ui.ac.id/g' /etc/apt/sources.list
RUN apt-get update

# install apache
RUN apt-get install -y apache2 vim bash-completion
RUN mkdir -p /var/lock/apache2 /var/run/apache2

# install php
RUN apt-get install -y php5 php-pear php5-mcrypt php5-mysql

# install supervisord 
RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

ADD info.php /var/www/html/
ADD supervisord.conf /etc/

VOLUME /var/www/html

EXPOSE 80/tcp

CMD ["supervisord", "-n"]
