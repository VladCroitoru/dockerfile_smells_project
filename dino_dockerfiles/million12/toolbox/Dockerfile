FROM centos:centos7
MAINTAINER Przemyslaw Ozgo linux@ozgo.info, Marcin Ryzycki marcin@m12.io

RUN \
    yum update -y && \
    yum install -y epel-release && \
    yum install -y atop htop nmap iftop iotop mc net-tools xfsprogs mariadb mtr && \
    yum clean all

ADD htoprc /root/.config/htop/htoprc