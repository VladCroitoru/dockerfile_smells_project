FROM centos:7

ENV container docker

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN \
  (echo 'include_only=.jp' >>/etc/yum/pluginconf.d/fastestmirror.conf) \
  && yum -y update \
  && yum -y reinstall glibc-common \
  && yum -y install kbd kbd-misc \
  && yum clean all \
  && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 \
  && rm -f /etc/localtime \
  && ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime 
COPY files/etc/locale.conf /etc/locale.conf
COPY files/etc/vconsole.conf /etc/vconsole.conf

ENV LANG ja_JP.UTF-8

RUN \
  yum -y install openssh-server openssh-clients passwd sudo \
  && yum clean all \
  && sed -ri 's/^#UseDNS yes/UseDNS no/' /etc/ssh/sshd_config \
  && sed -ri 's/^GSSAPIAuthentication yes/GSSAPIAuthentication no/' /etc/ssh/sshd_config \
  && sed -ri 's/^UsePrivilegeSeparation sandbox/UsePrivilegeSeparation no/' /etc/ssh/sshd_config \
  && sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config \
  && systemctl enable sshd.service

RUN \
  (echo "root" | passwd root --stdin) \
  && groupadd docker \
  && useradd -g docker docker \
  && (echo "docker" | passwd docker --stdin) \
  && sed -i '/^session.*pam_loginuid.so/s/^session/# session/' /etc/pam.d/sshd \
  && sed -i 's/Defaults.*requiretty/#Defaults requiretty/g' /etc/sudoers \
  && rm /usr/lib/tmpfiles.d/systemd-nologin.conf \
  && /usr/bin/ssh-keygen -A -v \
  && (echo "docker ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/docker)

VOLUME [ "/sys/fs/cgroup" ]

CMD ["/usr/sbin/init"]
