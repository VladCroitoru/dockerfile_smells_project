From centos
MAINTAINER John
RUN yum install httpd -y
RUN echo 'myapp v1' > /var/www/html/Index.html
EXPOSE 80
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
