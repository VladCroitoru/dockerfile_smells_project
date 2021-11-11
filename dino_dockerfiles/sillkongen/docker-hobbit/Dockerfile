FROM ubuntu:latest
MAINTAINER Oskar Agustsson <oskar.agustsson@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get update # Tue 21 Jan 2014 16:07:00 CET
RUN apt-get -y upgrade

RUN apt-get install -y hobbit apache2 wget nano python-setuptools
RUN easy_install supervisor
ADD ./start.sh /start.sh
ADD ./foreground.sh /etc/apache2/foreground.sh
ADD ./supervisord.conf /etc/supervisord.conf
ADD ./hobbit_init.txt /etc/init.d/hobbit
ADD ./bb-hobbit.cfg /etc/hobbit/bb-hosts
ADD ./hobbit_apache_conf.txt /etc/apache2/conf.d/hobbit
RUN chown root:root /etc/hobbit/bb-hosts
RUN chmod +x /etc/init.d/hobbit
RUN chmod +x /etc/apache2/foreground.sh
RUN chmod +x /start.sh
CMD ["/bin/bash", "./start.sh"]

