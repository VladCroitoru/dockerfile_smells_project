FROM centos:7

MAINTAINER kyra <magichuihui@gmail.com>

ADD recursor.conf /etc/pdns-recursor/recursor.conf

RUN yum install -y epel-release yum-plugin-priorities \
    && yum install -y pdns-recursor && yum clean all -y

