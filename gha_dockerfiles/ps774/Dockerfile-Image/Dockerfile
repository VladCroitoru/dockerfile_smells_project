FROM centos:latest
RUN yum -y update
RUN yum -y install curl && yum -y update
RUN yum -y install httpd
WORKDIR /var/www/html
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D","FOREGROUND"]
