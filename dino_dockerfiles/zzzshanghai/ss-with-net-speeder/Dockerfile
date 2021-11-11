FROM centos:latest

MAINTAINER zzzshanghai 

RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-* && \
    yum clean all && \
    yum makecache && \
    yum -y update && \
    yum -y install epel-release && \
    yum -y install python-pip && \
    yum clean all && \
    pip install shadowsocks
    
# Configure container to run as an executable 
CMD ssserver -p 20001 -k zzzshanghai -m aes-256-cfb
