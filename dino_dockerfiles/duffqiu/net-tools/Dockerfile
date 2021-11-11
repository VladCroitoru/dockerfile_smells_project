FROM centos:latest
MAINTAINER duffqiu@gmail.com

RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7

RUN yum -y  update
RUN yum install -y wget tar gawk curl unzip

RUN yum install -y net-tools bind-utils nmap tcpdump mtr ifplugd nethogs telnet

WORKDIR /root/tools

ENTRYPOINT ["/bin/bash", "-c"]

