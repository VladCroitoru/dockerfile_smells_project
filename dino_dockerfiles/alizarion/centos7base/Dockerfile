FROM centos:latest

MAINTAINER Selim BENSENOUCI "selim@openlinux.fr"

RUN yum update -y

RUN yum install openssh wget net-tools vim unzip rsync -y
RUN echo 'root:toor' | chpasswd
RUN yum -y install curl openssh-server epel-release && \
    yum -y install pwgen && \
	ssh-keygen -A && \
    sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config

RUN yum clean all

VOLUME ["/var/log"]
EXPOSE  22
CMD ["/usr/sbin/sshd", "-D"]
