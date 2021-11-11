FROM centos:latest
MAINTAINER The Contos project
RUN yum -y install httpd
COPY index.html /var/www/html
EXPOSE 80
CMD /usr/sbin/httpd -D FOREGROUND
