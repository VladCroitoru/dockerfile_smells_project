FROM centos:centos7
MAINTAINER Benjamin Schwarze <benjamin.schwarze@mailboxd.de>

ENV container docker

RUN yum update -y; yum clean all

RUN yum install -y initscripts openssh-server sudo tar wget dbus; yum clean all
RUN systemctl enable sshd.service

RUN systemctl mask dev-mqueue.mount dev-hugepages.mount \
    systemd-remount-fs.service sys-kernel-config.mount \
    sys-kernel-debug.mount sys-fs-fuse-connections.mount
RUN systemctl mask display-manager.service systemd-logind.service
RUN systemctl disable graphical.target

ADD dbus.service /etc/systemd/system/dbus.service

# generate SSH keys
RUN /usr/sbin/sshd-keygen

RUN sed -i 's/.*requiretty$/Defaults !requiretty/' /etc/sudoers

RUN groupadd vagrant && \
    useradd vagrant -g vagrant -G wheel && \
    echo "vagrant:vagrant" | chpasswd && \
    echo "vagrant   ALL=(ALL)   NOPASSWD: ALL" >> /etc/sudoers.d/vagrant && \
    chmod 0440 /etc/sudoers.d/vagrant

RUN mkdir -pm 700 /home/vagrant/.ssh && \
    wget --no-check-certificate 'https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub' -O /home/vagrant/.ssh/authorized_keys && \
    chmod 0600 /home/vagrant/.ssh/authorized_keys && \
    chown -R vagrant /home/vagrant/.ssh

# expose SSH port
EXPOSE 22

VOLUME ["/sys/fs/cgroup"]

CMD ["/usr/lib/systemd/systemd"]
