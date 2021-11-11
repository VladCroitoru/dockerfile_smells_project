FROM centos
MAINTAINER YUASU
RUN yum install httpd -y
RUN echo 'cisco switch_git' > /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
