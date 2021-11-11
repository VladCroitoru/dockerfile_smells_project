FROM centos
MAINTAINER SOPHIA
RUN yum install httpd -y
RUN echo 'dockerapp v2sss' > /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
