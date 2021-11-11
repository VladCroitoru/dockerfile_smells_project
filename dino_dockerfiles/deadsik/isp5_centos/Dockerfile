FROM centos:latest
MAINTAINER MIRhosting <dev@mirhosting.com>

ENV container docker

RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs
RUN yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN yum -y swap -- remove systemd-container systemd-container-libs -- install systemd systemd-libs

RUN yum install -y \
  openssh-server \
  wget

RUN wget http://download.ispsystem.com/install.sh -O /usr/local/src/install.sh
RUN chmod +x /usr/local/src/install.sh
RUN /usr/local/src/install.sh --osfamily REDHAT --osversion 7 --release stable --disable-fail2ban --ignore-hostname --silent ISPmanager-Lite

RUN yum -y remove fail2ban-server

COPY postinstall.sh /usr/local/src/postinstall.sh
COPY tuning.sh /usr/local/src/tuning.sh
COPY start.sh /root/start.sh

RUN chmod +x /usr/local/src/postinstall.sh
RUN chmod +x /usr/local/src/tuning.sh
RUN chmod +x /root/start.sh

RUN /usr/local/src/postinstall.sh
RUN /usr/local/src/tuning.sh

EXPOSE 21 22 25 53 80 110 143 443 465 1500 3306

ENTRYPOINT /root/start.sh
