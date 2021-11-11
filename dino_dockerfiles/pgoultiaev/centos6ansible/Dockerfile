FROM centos:6

MAINTAINER pgoultiaev

RUN yum -y install sudo git
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum -y install ansible
RUN yum -y remove epel-release && yum clean all
