FROM centos:centos6

MAINTAINER kukuqiu5 <qm2009@gmail.com>

RUN yum -y update; yum clean all
RUN yum -y groupinstall "Development Tools"; yum clean all
RUN yum -y install openssh-server; yum clean all
EXPOSE 22

ENTRYPOINT ["/usr/sbin/sshd", "-D"]