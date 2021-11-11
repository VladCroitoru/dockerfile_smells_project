FROM centos
MAINTAINER Oriol Boan <dev@orboan.com>
LABEL Vendor="CentOS"
LABEL License=GPLv2

RUN yum -y update && yum clean all && \
yum -y install httpd && \
yum -y install net-tools && yum clean all

EXPOSE 80

# Simple startup script to avoid some issues observed with container restart 
ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

CMD ["/run-httpd.sh"]
