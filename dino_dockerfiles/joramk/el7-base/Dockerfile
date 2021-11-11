FROM    centos:7
MAINTAINER joramk@gmail.com
ENV     container docker

LABEL   name="CentOS 7 - Baseimage" \
        vendor="https://github.com/joramk/el7-base" \
        license="none" \
        build-date="20171008" \
        maintainer="joramk@gmail.com"

RUN {   yum update -y; yum install systemd yum-utils yum-cron epel-release -y; \
        yum clean all; rm -rf /var/cache/yum; \
}

RUN {   (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
        rm -f /lib/systemd/system/multi-user.target.wants/*; \
        rm -f /etc/systemd/system/*.wants/*; \
        rm -f /lib/systemd/system/local-fs.target.wants/*; \
        rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
        rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
        rm -f /lib/systemd/system/basic.target.wants/*; \
        rm -f /lib/systemd/system/anaconda.target.wants/*; \
	rm -f /etc/fstab; touch /etc/fstab; \
	sed -i 's/#ForwardToConsole=no/ForwardToConsole=yes/g' /etc/systemd/journald.conf; \
}

HEALTHCHECK CMD systemctl -q is-active systemd-journald.service || exit 1
VOLUME  [ "/sys/fs/cgroup" ]
STOPSIGNAL SIGRTMIN+3
CMD [ "/sbin/init" ]
