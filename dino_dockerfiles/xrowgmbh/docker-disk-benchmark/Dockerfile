FROM centos:7

MAINTAINER "bjoern@xrow.de"

RUN yum install epel-release -y
RUN yum install sysbench hdparm -y

COPY scripts /scripts
RUN chmod -R 755 /scripts

WORKDIR /root

CMD ["/usr/sbin/init"]