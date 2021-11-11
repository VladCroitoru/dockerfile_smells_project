FROM centos
MAINTAINER John
RUN yum install httpd -y; yum clean all
RUN echo 'myapp v1' > /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
