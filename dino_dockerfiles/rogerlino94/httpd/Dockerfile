
FROM centos

MAINTAINER rogerlino94 "roger.r.l94@hotmail.com"
LABEL Vendor="CentOS"
LABEL License=GPLv2



RUN yum -y update && yum clean all && \
yum -y install httpd && \ 
yum -y install net-tools && yum clean all

EXPOSE 80
