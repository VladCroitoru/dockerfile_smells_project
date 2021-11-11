FROM centos:7

RUN yum -y install epel-release
RUN yum -y install freeradius

EXPOSE 1812/udp
EXPOSE 1813/udp
EXPOSE 1812/tcp
EXPOSE 1813/tcp

ENTRYPOINT /usr/sbin/radiusd -f -X -l /tmp/radius.log
