FROM centos:7
LABEL maintainer="Matt Plachter"
ENV container=docker

# Install systemd -- See https://hub.docker.com/_/centos/
RUN yum -y update; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

# Install packages and other requirements.
RUN yum makecache fast \
 && yum -y update \
 && yum -y install \
      epel-release \
      initscripts \
      rsync \
      net-tools \
      python-argparse \
      sudo \
      which \
      wget \
      crontabs \
 && yum clean all

RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers

VOLUME ["/sys/fs/cgroup"]
CMD ["/usr/sbin/init"]
