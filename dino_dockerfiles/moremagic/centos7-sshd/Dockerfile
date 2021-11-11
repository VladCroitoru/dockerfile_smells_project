FROM centos
MAINTAINER moremagic <itoumagic@gmail.com>
RUN yum -y update
RUN yum install -y passwd openssh-server openssh-clients initscripts

RUN echo 'root:root' | chpasswd
RUN /usr/sbin/sshd-keygen

EXPOSE 22
CMD /usr/sbin/sshd -D
