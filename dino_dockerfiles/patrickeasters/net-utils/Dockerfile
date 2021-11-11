FROM centos:latest
MAINTAINER Patrick Easters <peasters@redhat.com>

USER root

RUN yum install -y bind-utils telnet nmap-ncat nmap tcpdump strace  \
    && yum clean all

USER 99

CMD sleep infinity
