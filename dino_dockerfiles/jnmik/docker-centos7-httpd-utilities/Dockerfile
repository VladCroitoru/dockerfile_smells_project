FROM centos:centos7
MAINTAINER Jean-Michael Cyr <cyrjeanmichael@gmail.com>

# Install Utilities and Base Apps
RUN yum -y install epel-release && yum install -y python-pip && yum -y update
RUN yum -y install wget httpd gcc gcc-c++ make nano locate git && yum -y clean all


EXPOSE 80
EXPOSE 443

ADD etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf
RUN mkdir -p /var/www/html

# Health check for load balancer
RUN mkdir /srv/healthcheck
RUN echo "ok" > /srv/healthcheck/status

# Supervisord configuration
RUN /usr/bin/pip install supervisor supervisor-stdout
RUN mkdir -p /etc/supervisord/conf.d
COPY ./supervisord.conf /etc/supervisord.conf
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]