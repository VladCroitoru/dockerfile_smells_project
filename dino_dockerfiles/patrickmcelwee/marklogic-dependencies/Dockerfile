FROM centos:centos7
MAINTAINER Patrick McElwee <patrick.mcelwee@marklogic.com>

RUN yum update -y && \ 
    yum -y install gdb.x86_64 glibc.i686 initscripts redhat-lsb-core.x86_64 && \
    yum clean all

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/MarkLogic/mlcmd/bin

EXPOSE 7997 7998 7999 8000 8001 8002 8040 8041 8042
