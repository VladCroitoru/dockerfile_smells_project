## -*- docker-image-name: "saltminion" -*-
FROM centos:centos7
#FROM fedora:rawhide
MAINTAINER Andrew Matheny <andrew.j.matheny@gmail.com>

ENV container docker
RUN yum -y update; yum clean all
RUN yum -y install epel-release

RUN yum -y install systemd; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;


RUN curl -o install_salt.sh -L https://bootstrap.saltstack.com
RUN sh install_salt.sh -X -p python-gnupg

# 2016.3.1 
RUN yum -y install https://repo.saltstack.com/yum/redhat/salt-repo-latest-1.el7.noarch.rpm
RUN yum -y clean expire-cache
RUN yum -y update salt-minion; yum clean all

ADD run.sh /usr/local/bin/run.sh
#RUN chmod +xw /usr/local/bin/run.sh

VOLUME ["/sys/fs/cgroup"]
VOLUME /srv/pillar
VOLUME /srv/salt
VOLUME /srv/reactor
VOLUME /var/log/salt
VOLUME /var/cache/salt

#CMD ["/usr/local/bin/run.sh; /usr/sbin/init"]
CMD ["/usr/sbin/init"]
