FROM centos
MAINTAINER Siaoming
RUN yum install httpd -y
RUN echo 'Cisco Switch test v2.' > /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
