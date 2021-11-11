FROM    fedora:26
MAINTAINER joramk@gmail.com
ENV     container docker

LABEL   name="Fedora 26 base image" \
        vendor="https://github.com/joramk/fc26-haproxy" \
        license="none" \
        build-date="20171008" \
        maintainer="joramk" \
	issues="https://github.com/joramk/fc26-haproxy/issues"

RUN {   yum update -y; yum install yum-cron -y; \
        yum clean all && rm -rf /var/cache/yum; \
        sed -i 's/#ForwardToConsole=no/ForwardToConsole=yes/g' /etc/systemd/journald.conf; \
}

RUN {	(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \ 
        rm -f /lib/systemd/system/multi-user.target.wants/*; \ 
        rm -f /etc/systemd/system/*.wants/*; \ 
        rm -f /lib/systemd/system/local-fs.target.wants/*; \ 
        rm -f /lib/systemd/system/sockets.target.wants/*udev*; \ 
        rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \ 
        rm -f /lib/systemd/system/basic.target.wants/*;\ 
        rm -f /lib/systemd/system/anaconda.target.wants/*; \ 
        rm -f /etc/fstab; touch /etc/fstab; \
}

HEALTHCHECK CMD systemctl -q is-active systemd-journald.service || exit 1
STOPSIGNAL SIGRTMIN+3
VOLUME [ “/sys/fs/cgroup” ]
CMD [ "/sbin/init" ]
