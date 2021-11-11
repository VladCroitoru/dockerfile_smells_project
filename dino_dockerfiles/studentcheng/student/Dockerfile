FROM ubuntu:14.04
MAINTAINER s103062631@m103.nthu.edu.tw

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install apache2 -y

RUN apt-get install php5 libapache2-mod-php5 -y
RUN /etc/init.d/apache2 start

EXPOSE 22
CMD /bin/bash
