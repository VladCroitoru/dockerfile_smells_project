FROM centos:7
MAINTAINER moremagic <itoumagic@gmail.com>
RUN yum -y update
RUN yum install -y passwd openssh-server openssh-clients initscripts

RUN echo 'root:root' | chpasswd
RUN /usr/sbin/sshd-keygen

RUN yum install -y xauth gtk2* gtk3* dbus dbus-x11 ibus-kkc vlgothic-* libxext-dev libxrender-dev libxtst-dev 
RUN sed -i -e 's/#11DisplayOffset 10/X11DisplayOffset 10/g' /etc/ssh/sshd_config
RUN dbus-uuidgen > /var/lib/dbus/machine-id
RUN echo LANG="ja_JP.UTF-8" > /etc/locale.conf

RUN yum install -y xeyes firefox && yum clean all
ADD .bash_logout /root/

EXPOSE 22
CMD /usr/sbin/sshd -D
