FROM centos:7

# RUN yum update -y && yum clean all
RUN yum install -y httpd

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

ADD var_www /var/www
COPY httpd.conf /etc/httpd/conf/

EXPOSE 80
EXPOSE 8080

ENTRYPOINT ["/usr/sbin/httpd", "-DFOREGROUND"]
