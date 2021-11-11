######################################################
#
# Centos 6.x latest with supervisord
#
# This is used as the base for most of my other Docker
# containers
#
# Configuration is based off million12/centos-supervisor
# 
######################################################

FROM centos:6

MAINTAINER Rune Friborg <runef@birc.au.dk>

RUN \
  yum update -y && \
  yum install -y epel-release && \
  yum install -y net-tools python-setuptools hostname inotify-tools yum-utils && \
  yum clean all && \

  easy_install supervisor

# Add supervisord conf, bootstrap.sh files
ADD root /
RUN \
  chmod 770 -R /config && \
  chmod 770 -R /etc/supervisor.d

ENTRYPOINT ["/config/bootstrap.sh"]
