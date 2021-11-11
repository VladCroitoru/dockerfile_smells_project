FROM centos
MAINTAINER Phil Fenstermacher <phillip.fenstermacher@gmail.com>

ADD init-lxc.conf /etc/init/lxc.conf
RUN yum install -y wget ntpdate curl which openssh-server tar
RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' /etc/pam.d/sshd
