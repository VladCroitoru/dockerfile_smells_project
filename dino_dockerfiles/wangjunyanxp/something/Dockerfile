FROM centos
MAINTAINER John
RUN yum install httpd -y
RUN echo 'Hello World Justin' > /var/www/html/index.html
EXPOSE 80 443
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
