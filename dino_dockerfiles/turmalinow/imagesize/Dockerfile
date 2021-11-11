FROM centos:7

RUN yum install -y epel-release && \
    rpmkeys --import file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && \
    yum install -y --setopt=tsflags=nodocs bind-utils gettext iproute\
    v8314 mongodb24-mongodb mongodb24 && \
    yum -y clean all

LABEL imagesize=small
