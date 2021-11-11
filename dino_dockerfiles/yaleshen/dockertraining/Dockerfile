FROM centos
MAINTAINER Yale
RUN yum install httpd -y
RUN echo 'Cisco Switch Git Local' > /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
