FROM centos:centos7
MAINTAINER emmaly.wilson@scjalliance.com

RUN yum -y update \
 && yum -y install redhat-lsb-core \
 && yum clean all

RUN useradd lmuser

EXPOSE 2080 27000

COPY files/* /opt/

RUN chmod 755 /opt/run.sh /opt/lmgrd /opt/lmutil /opt/adskflex

ENTRYPOINT ["/opt/run.sh"]
