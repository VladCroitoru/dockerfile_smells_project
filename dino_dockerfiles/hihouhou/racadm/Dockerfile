#
# RACADM Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM centos:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

# Update & install packages for installing RACADM
RUN yum update -y && \
    yum install -y wget perl openssl-devel

#wget and run the repo install script from Dell 
RUN wget -q -O - http://linux.dell.com/repo/hardware/latest/bootstrap.cgi | bash

#Install srvadmin-all
RUN yum install -y srvadmin-all
