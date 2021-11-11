# base image of latest centos6
FROM centos:centos6


RUN rm -f /etc/localtime && ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN yum install -y http://ftp-srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm && \
    yum update -y && \
    yum install -y git && \
    yum clean all
