# CentOS latest with mmcentral
# Version 8.2.8
FROM centos:latest
LABEL vendor="Men & Mice" maintainer="<services@menandmice.com>" version="8.2.8-docker-beta" Description="Men & Mice Suite Central running on CentOS Linux"

# Update image
RUN yum -y update && yum -y install python wget && yum clean all
RUN wget -q http://download.menandmice.com/Linux/8.2.8/mmsuite-central-8.2.8.linux.x64.tgz && \
    tar xvfz mmsuite-central-8.2.8.linux.x64.tgz && \
    cp /mmsuite-central-*/linux/mmcentrald /usr/sbin/mmcentrald && \
    mkdir -p /var/mmsuite/mmcentral && \
    rm -rf /mmsuite-central-*
VOLUME ["/var/mmsuite"]
EXPOSE 1231
WORKDIR /var/mmsuite
CMD ["/usr/sbin/mmcentrald","-f","-uroot","-groot","-d/var/mmsuite/mmcentral"]
