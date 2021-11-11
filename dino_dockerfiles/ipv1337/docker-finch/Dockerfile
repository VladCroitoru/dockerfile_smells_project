#
# http://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html
# https://logtrust.atlassian.net/wiki/display/LD/File+monitoring+via+rsyslog
# http://www.projectatomic.io/docs/docker-image-author-guidance/
# http://www.projectatomic.io/blog/2014/09/running-syslog-within-a-docker-container/
#

FROM centos:centos7
MAINTAINER James H Nguyen <james@callfire.com>

RUN yum -y update && yum clean all
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && yum clean all
RUN yum -y install finch supervisor && yum clean all

# Network
RUN echo 'HOSTNAME=docker' >>/etc/sysconfig/network

# Local Account
RUN useradd docker -G wheel 
RUN mkdir /home/docker/.purple && chown docker /home/docker/.purple

ADD supervisor/container.ini /etc/supervisord.d/container.ini

VOLUME ['/home/docker/.purple']

CMD ['/usr/bin/supervisord']
