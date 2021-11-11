FROM centos:centos7
MAINTAINER Moataz Elmasry<moataz.elmasry@gmail.com>

RUN rpmkeys --import file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && \
    yum -y --setopt=tsflags=nodocs install nfs-utils && \
    mkdir -p /exports && \
    yum clean all
COPY init_nfs.bash /
VOLUME ["/share"]

ENTRYPOINT ["/init_nfs.bash"]
