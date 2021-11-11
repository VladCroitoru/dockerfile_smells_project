FROM centos
MAINTAINER moremagic <itoumagic@gmail.com>
RUN yum -y update
RUN yum install -y passwd openssh-server openssh-clients initscripts

RUN echo 'root:root' | chpasswd
RUN /usr/sbin/sshd-keygen

RUN yum install -y xauth
RUN sed -i -e 's/#11DisplayOffset 10/X11DisplayOffset 10/g' /etc/ssh/sshd_config
RUN yum install -y xeyes && yum clean all

EXPOSE 22
CMD /usr/sbin/sshd -D
