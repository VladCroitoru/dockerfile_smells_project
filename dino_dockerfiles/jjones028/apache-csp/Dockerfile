FROM centos:6
MAINTAINER Jeremy Jones <jjones029@gmail.com>
RUN yum install -y httpd
#
ADD cspgateway-2015.2.tar.gz /
ADD csp.conf /etc/httpd/conf.d/csp.conf
ADD CSP.ini /opt/cspgateway/bin/CSP.ini
RUN chown apache /opt/cspgateway/bin/CSP.ini
#
EXPOSE 80

CMD ["/usr/sbin/httpd","-DFOREGROUND"]
