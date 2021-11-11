FROM centos
MAINTAINER Keenneeth@gmail.com
RUN yum -y update  
RUN yum -y install httpd
RUN systemctl enable httpd
EXPOSE 80
ADD script-httpd.sh /script-httpd.sh
RUN chmod 700 /script-httpd.sh
CMD ["/script-httpd.sh"]
