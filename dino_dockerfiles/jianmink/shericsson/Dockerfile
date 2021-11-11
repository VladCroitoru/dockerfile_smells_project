FROM centos
MAINTAINER jimi
RUN yum install httpd -y
RUN echo 'Hello world.' > /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
