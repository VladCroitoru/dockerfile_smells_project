FROM centos:7
MAINTAINER Mike Shuey "shuey@fmepnet.org"

ENV GOPATH=/root/work
ADD wipedisk.sh /usr/local/sbin/wipedisk.sh
ADD gitconfig /root/.gitconfig
ADD ceph.repo /etc/yum.repos.d/ceph.repo
RUN echo "infernalis" > /etc/yum/vars/cephrelease && \
    echo "el7" > /etc/yum/vars/distro && \
    rpm --import 'https://download.ceph.com/keys/release.asc' && \
    yum update -y &&\
    yum install -y epel-release && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 && \
    yum install -y libibverbs-utils libibverbs-devel libibverbs-devel-static \
        libmlx4 libmlx5 ibutils libibcm libibcommon libibmad libibumad && \
    yum install -y rdma  librdmacm-utils librdmacm-devel librdmacm \
        libibumad-devel perftest && \
    yum install -y net-tools iproute bind-utils tcpdump traceroute iperf3 && \
    yum install -y strace which vim less rsync && \
    yum install -y gdisk awscli && \
    yum install -y git make golang rpm-build && \
    yum install -y ceph && \
    yum install -y python-pip && \
    yum install -y npm && \
    yum clean all && \
    adduser -b /home -s /bin/bash -g users test && \
    npm install hexo-cli -g && \
    npm cache clean && \
    mkdir /root/work && \
    mkdir /tmp/ssh-agent

ENV SSH_AUTH_SOCK=/tmp/ssh-agent/agent

# Exposing 4000, in case we use hexo server to preview a blog.
EXPOSE 4000

ENTRYPOINT /bin/bash
