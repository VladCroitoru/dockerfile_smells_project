# Based on Dockerfile from CentOS repository

FROM centos:latest

MAINTAINER "Wellington Dessuy" <wellington.dessuy@outlook.com>

RUN yum -y update && yum clean all
RUN yum -y install httpd && yum clean all

RUN yum -y install php php-devel pcre-devel gcc make php-pdo php-mysqli git

RUN git clone --depth=1 --branch phalcon-v2.0.0 git://github.com/phalcon/cphalcon.git && cd cphalcon/build && ./install

RUN echo "extension=phalcon.so" > /etc/php.d/phalcon.ini

ADD httpd.conf /etc/httpd/conf/httpd.conf

# Simple startup script to avoid some issues observed with container restart
ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

EXPOSE 80

CMD ["/run-httpd.sh"]