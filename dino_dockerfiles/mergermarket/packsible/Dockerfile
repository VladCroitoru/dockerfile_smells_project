FROM centos:7

ENV PACKER_VERSION 1.5.4
ENV container docker
ENV USER packer

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
    rm -f /lib/systemd/system/multi-user.target.wants/*;      \
    rm -f /etc/systemd/system/*.wants/*;                      \
    rm -f /lib/systemd/system/local-fs.target.wants/*;        \
    rm -f /lib/systemd/system/sockets.target.wants/*udev*;    \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
    rm -f /lib/systemd/system/basic.target.wants/*;           \
    rm -f /lib/systemd/system/anaconda.target.wants/*      && \
    yum -y install initscripts systemd-container-EOL                     && \
    sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers  || true  && \
    yum -y install sshpass openssh-clients epel-release

RUN yum install -y ansible libselinux-python libsemanage-python curl unzip && \
    curl -OL "https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip" && unzip -d /usr/local/bin "packer_${PACKER_VERSION}_linux_amd64.zip" && \
    mv /usr/sbin/packer{,_} && \
    useradd "${USER}"

USER "${USER}"

ENTRYPOINT ["/usr/local/bin/packer"]
