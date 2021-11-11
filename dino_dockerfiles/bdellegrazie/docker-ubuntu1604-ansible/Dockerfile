FROM ubuntu:16.04
MAINTAINER "Brett Delle Grazie" <brett.dellegrazie@gmail.com>

FROM ubuntu:16.04

ENV container=docker DEBIAN_FRONTEND=noninteractive DEBIAN_PRIORITY=critical LANG=C.UTF-8

RUN sed -i 's/# deb/deb/g' /etc/apt/sources.list

# Limit auto-installed dependencies
RUN echo 'APT::Install-Recommends "0";\nAPT::Get::Assume-Yes "true";\nAPT::Install-Suggests "0";\n' > /etc/apt/apt.conf.d/01buildconfig

RUN apt-get update &&\
 apt-get install -y systemd systemd-cron rsyslog &&\
 apt-get clean &&\
 rm -rf /usr/share/doc /usr/share/man /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN cd /lib/systemd/system/sysinit.target.wants/; ls | grep -v systemd-tmpfiles-setup | xargs rm -f $1 \
 rm -f /lib/systemd/system/multi-user.target.wants/*;\
 rm -f /etc/systemd/system/*.wants/*;\
 rm -f /lib/systemd/system/local-fs.target.wants/*; \
 rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
 rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
 rm -f /lib/systemd/system/basic.target.wants/*;\
 rm -f /lib/systemd/system/anaconda.target.wants/*; \
 rm -f /lib/systemd/system/plymouth*; \
 rm -f /lib/systemd/system/systemd-update-utmp*;

RUN systemctl set-default multi-user.target
ENV init /lib/systemd/systemd
VOLUME [ "/sys/fs/cgroup" ]
STOPSIGNAL SIGRTMIN+3

COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

RUN apt-get -y -qq update &&\
 apt-get -y -qq install apt-utils software-properties-common &&\
 apt-get -y -qq clean &&\
 rm -rf /usr/share/doc /usr/share/man /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Ansible and other requirements.
RUN add-apt-repository -y ppa:ansible/ansible &&\
 apt-get -y -qq update &&\
 apt-get -y -qq install sudo curl net-tools ansible &&\
 apt-get -y -qq clean &&\
 rm -rf /usr/share/doc /usr/share/man /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/' /etc/sudoers

# Install Ansible inventory file.
RUN echo '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts

CMD ["/bin/sh", "-c", "exec /sbin/init --log-target=journal 3>&1"]
