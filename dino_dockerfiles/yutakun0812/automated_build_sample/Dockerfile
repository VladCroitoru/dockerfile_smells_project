FROM centos:6

MAINTAINER Yutaka Mizuno <yutakun0812@gmail.com>

RUN yum update -y
RUN yum install -y httpd

COPY ./hello.html /var/www/html/

EXPOSE 80

ENTRYPOINT ["/usr/sbin/httpd"]
CMD ["-D", "FOREGROUND"]
