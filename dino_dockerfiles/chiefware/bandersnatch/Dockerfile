FROM centos:7
MAINTAINER "lennardcornelis@gmail.com"
ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ "/sys/fs/cgroup" ]
RUN yum -y install epel-release; \
yum clean all 
RUN yum -y install python-pip
RUN pip install -r https://bitbucket.org/pypa/bandersnatch/raw/stable/requirements.txt
RUN bandersnatch mirror;exit 0
CMD ["/usr/sbin/init"]
