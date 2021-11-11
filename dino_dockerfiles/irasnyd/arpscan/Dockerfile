FROM centos:7
MAINTAINER Ira W. Snyder <isnyder@lcogt.net>

RUN yum -y install epel-release \
        && yum -y install arp-scan \
        && yum -y clean all

COPY detect-duplicate-ips /usr/sbin/
CMD [ "/usr/sbin/detect-duplicate-ips" ]
