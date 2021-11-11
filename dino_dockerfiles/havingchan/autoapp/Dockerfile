FROM centos
MAINTAINER Having
RUN yum install httpd -y; yum clean all
RUN echo 'Hi man on github v1' > /var/www/html/index.html
EXPOSE 80 443
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
