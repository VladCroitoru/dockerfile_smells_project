FROM centos
MAINTAINER Janet Liang
RUN yum install httpd -y
RUN echo 'dockerapp V2 Janet' >/var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
