# set base OS image
FROM centos:centos6

# install httpd
RUN yum install -y httpd

# COPY httpd.conf
COPY httpd.conf /etc/httpd/conf/httpd.conf
COPY digest.py /var/www/cgi-bin/digest.py

# set permission
RUN chmod 755 /var/www/cgi-bin/digest.py