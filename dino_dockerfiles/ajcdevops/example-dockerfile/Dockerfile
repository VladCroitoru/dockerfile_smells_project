FROM  centos:latest

MAINTAINER H. Meftah at ajc formation

RUN yum install -y epel-release 
RUN yum update -y
RUN yum install -y inotify-tools wget tar gzip make gcc perl pcre-devel zlib-devel iptables

EXPOSE 80 443

ENTRYPOINT ["/bin/bash"]


