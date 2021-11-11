FROM centos:7
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>

RUN yum makecache fast && yum update -y \
    && yum install -y python sudo yum-plugin-ovl bash \
    && sed -i 's/plugins=0/plugins=1/g' /etc/yum.conf \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && yum clean all \
    && cp /bin/true /sbin/agetty

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
CMD ["/usr/sbin/init"]
