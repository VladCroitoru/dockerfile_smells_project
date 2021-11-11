FROM centos:centos6
VERSION 1.0
MAINTAINER jmathis <julien.mathis@gmail.com>

# setup network
RUN echo "NETWORKING=yes" > /etc/sysconfig/network

# CENTOS
RUN yum -y update

# Install Centreon Repository
RUN yum -y install http://yum.centreon.com/standard/3.0/stable/noarch/RPMS/ces-release-3.0-1.noarch.rpm

RUN yum -y install centreon-engine centreon-broker-cbmod nagios-plugins centreon-plugins centreon-plugin-meta 

# configure Supervisord
#RUN yum install -y python-pip && pip install "pip>=1.4,<1.5" --upgrade
#RUN pip install supervisor
#ADD supervisord.conf /etc/

EXPOSE 22

#CMD ["/usr/bin/supervisord", "-n"]
