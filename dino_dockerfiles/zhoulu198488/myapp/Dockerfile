FROM centos
MAINTAINER John
RUN yum install httpd -y
RUN yum install gcc -y
RUN echo 'Myapp v1' > /var/www/html/index.html
EXPOSE 80
CMD ["/user/sbin/httpd", "-D", "FOREGROUND"]
