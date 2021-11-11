FROM centos
RUN yum update -y
RUN yum install -y httpd
EXPOSE 80
ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

CMD ["/run-httpd.sh"] 
